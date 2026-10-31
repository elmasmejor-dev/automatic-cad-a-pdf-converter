"""Mejora acotada de impresión prolongada AutoCAD COM; base v7.2.10."""
from pathlib import Path
import sys

BLOCK = '''def detalle_error_plot(exc):
    """Expone detalles de pywin32 que normalmente se pierden al mostrar el error."""
    pieces=[f'{type(exc).__name__}: {exc}']
    codes=[]
    for h in (getattr(exc,'hresult',None), exc.args[0] if getattr(exc,'args',()) else None):
        if isinstance(h,int):codes.append(f'0x{h & 0xffffffff:08X}')
    if codes:pieces.append('HRESULT '+', '.join(dict.fromkeys(codes)))
    info=getattr(exc,'excepinfo',None)
    if info is None and len(getattr(exc,'args',()))>=3:
        info=exc.args[2]
    if isinstance(info,(tuple,list)):
        if len(info)>2 and info[2]:pieces.append('Descripción: '+str(info[2])[:350])
        if len(info)>1 and info[1]:pieces.append('Origen: '+str(info[1])[:120])
        if len(info)>5 and isinstance(info[5],int):pieces.append(f'SCODE 0x{info[5] & 0xffffffff:08X}')
    return '; '.join(pieces)


def error_del_servidor_com(exc):
    """El error COM de PlotToFile puede ser temporal incluso sin código RPC busy.

    No tratamos errores arbitrarios de Python como COM recuperables.
    """
    if es_com_ocupado(exc):return True
    if isinstance(getattr(exc,'hresult',None),int):return True
    if type(exc).__name__=='com_error':return True
    return False


def recuperar_ploteo_despues_de_com(doc,app,marco,informar,papel,sin_visor):
    """Recupera contexto tras fallo de trazado sin reabrir ni guardar el DXF."""
    if app is None or marco is None:return
    activar_documento(app,doc,informar)
    reintentar_com(lambda:doc.SetVariable('BACKGROUNDPLOT',0),
                   'restablecer impresión en primer plano',informar)
    config=reintentar_com(lambda:configurar_ploteo(doc,marco,sin_visor=sin_visor,papel=papel),
                          'reconfigurar trazador PDF',informar)
    diagnostico_impresion('Recuperación COM: dibujo activado; BACKGROUNDPLOT=0; PC3='+str(config))
    pausa_autocad(.8)


def plotear_con_recuperacion(doc, archivo_temporal, informar, intentos=6,
                             *, app=None, marco=None, papel='Auto', sin_visor=False):
    """Imprime exactamente una página por intento; recupera fallos COM tardíos.

    Antes de reintentar se busca si el PDF existe y es válido. Nunca se vuelve a
    usar el nombre de archivo de un intento anterior, para evitar duplicados.
    """
    base=Path(archivo_temporal)
    ultimo='sin información'
    diagnostico_impresion(f'Inicio de lámina {base.name}; intentos={intentos}')
    for intento in range(1,intentos+1):
        path=base.with_name(f'{base.stem}_intento_{intento}{base.suffix}')
        try:
            # Si existe un archivo residual con este nombre, nunca aceptarlo.
            if path.exists():path.unlink()
            # Una referencia Plot fresca en cada intento evita reutilizar un
            # proxy COM de un trazado previo que ya terminó.
            plot=reintentar_com(lambda:doc.Plot,'obtener objeto de impresión',informar)
            enviado=plot.PlotToFile(str(path))
            if esperar_pdf_completo(path,10.0 if enviado else 3.5):
                diagnostico_impresion(f'{base.name} intento {intento}: PlotToFile={enviado!r}; PDF correcto')
                return path
            _,detalle=estado_pdf_temporal(path)
            ultimo=f'PlotToFile={enviado!r}; {detalle}'
            diagnostico_impresion(f'{base.name} intento {intento}/{intentos}: {ultimo}')
        except Exception as exc:
            detalle=detalle_error_plot(exc)
            diagnostico_impresion(f'{base.name} intento {intento}/{intentos}: EXCEPCIÓN: {detalle}')
            if not error_del_servidor_com(exc):
                raise
            # El trazado pudo finalizar antes de devolver la excepción COM.
            if esperar_pdf_completo(path,4.0):
                diagnostico_impresion(f'{base.name} intento {intento}: COM devolvió error pero el PDF es válido')
                return path
            estado=estado_pdf_temporal(path)[1]
            ultimo=f'{detalle}; PDF: {estado}'
        if intento==intentos:break
        informar(f'AutoCAD no completó la lámina; recuperando impresión ({intento}/{intentos}).')
        # Reaplicar el marco solo si se dispone del contexto completo; hacerlo
        # después de comprobar que NO apareció el PDF anterior.
        try:
            recuperar_ploteo_despues_de_com(doc,app,marco,informar,papel,sin_visor)
        except Exception as recovery_exc:
            descripcion=detalle_error_plot(recovery_exc)
            diagnostico_impresion(f'{base.name}: no se pudo recuperar trazador: {descripcion}')
            if not error_del_servidor_com(recovery_exc):
                raise RuntimeError('AutoCAD no pudo restaurar el trazador: '+descripcion) from recovery_exc
            ultimo+='; al recuperar trazador: '+descripcion
        pausa_autocad(min(0.8+0.55*intento,3.2))
    raise RuntimeError(
        f'AutoCAD no generó la página después de {intentos} intentos de recuperación. '
        f'Último resultado: {ultimo}. Revisa el registro en '
        '%LOCALAPPDATA%\\AutomaticCadPDFConverter\\diagnostico_impresion.txt '
        'y prueba imprimir esta lámina sola desde AutoCAD.')


'''
def patch(path):
    p=Path(path)
    text=p.read_text(encoding='utf-8')
    assert text.count('VERSION = "7.2.10"')==1,'La base debe ser v7.2.10'
    assert text.count('def plotear_con_recuperacion(')==1
    start=text.index('def plotear_con_recuperacion(')
    end=text.index('def conectar_autocad(',start)
    text=text[:start]+BLOCK+text[end:]
    old='parts=plotear_con_recuperacion(d,name,informar)'
    assert text.count(old)==1
    text=text.replace(old,"parts=plotear_con_recuperacion(\n                            d,name,informar,app=app,marco=r,\n                            papel=papel,sin_visor=no_abrir_visor)")
    old='''                    pausa_autocad(.18)'''
    assert text.count(old)==1
    text=text.replace(old,'''                    # Dar a AutoCAD tiempo de liberar trabajos de impresión tras
                    # cada grupo de páginas sin ralentizar excesivamente lotes cortos.
                    pausa_autocad(1.2 if procesadas % 12==0 else .22)''')
    current='''            reader=PdfReader(str(path),strict=False)
            count=len(reader.pages)
            if count != 1:return False,f'PDF con {count} páginas en vez de 1'
            mediabox=reader.pages[0].mediabox
            if float(mediabox.width)<=0 or float(mediabox.height)<=0:
                return False,'página con dimensiones inválidas'
            return True,f'PDF verificado ({size} bytes, una página)'
'''
    modified='''            with path.open('rb') as stream:
                reader=PdfReader(stream,strict=False)
                count=len(reader.pages)
                if count != 1:return False,f'PDF con {count} páginas en vez de 1'
                mediabox=reader.pages[0].mediabox
                if float(mediabox.width)<=0 or float(mediabox.height)<=0:
                    return False,'página con dimensiones inválidas'
            return True,f'PDF verificado ({size} bytes, una página)'
'''
    assert text.count(current)==1
    text=text.replace(current,modified)
    text=text.replace('VERSION = "7.2.10"','VERSION = "7.2.11"')
    compile(text,str(p),'exec')
    p.write_text(text,encoding='utf-8')
    print('Parche v7.2.11: recuperación COM, diagnóstico y liberación de lector PDF')

if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit('Uso: patch_plot_7211.py automatic_cad_to_pdf.py')
    patch(sys.argv[1])
