"""Mejora el trazado PDF de la versión empaquetada 7.2.6."""
import argparse
from pathlib import Path

HEADER = '''def diagnostico_impresion(mensaje):
    """Guarda los resultados del trazado fuera de la carpeta temporal."""
    try:
        base = Path(os.environ.get('LOCALAPPDATA', tempfile.gettempdir())) / 'AutomaticCadPDFConverter'
        base.mkdir(parents=True, exist_ok=True)
        registro = base / 'diagnostico_impresion.txt'
        if registro.is_file() and registro.stat().st_size > 1024 * 1024:
            registro.replace(base / 'diagnostico_impresion_anterior.txt')
        from datetime import datetime
        with registro.open('a', encoding='utf-8') as out:
            out.write(datetime.now().isoformat(timespec='seconds') + '  ' + str(mensaje) + '\\n')
    except OSError:
        pass


def estado_pdf_temporal(ruta):
    """Admite PDFs recuperables, pero exige exactamente una página válida."""
    path=Path(ruta)
    try:
        if not path.is_file():return False,'archivo no creado'
        size=path.stat().st_size
        if size < 100:return False,f'archivo demasiado pequeño ({size} bytes)'
        with path.open('rb') as f:
            inicio=f.read(1024)
            f.seek(max(0,size-4096))
            final=f.read()
        if b'%PDF-' not in inicio:return False,f'cabecera PDF ausente ({size} bytes)'
        if b'%%EOF' not in final:return False,f'PDF sin marca EOF ({size} bytes; quizás aún escribiéndose)'
        try:
            from pypdf import PdfReader
            reader=PdfReader(str(path),strict=False)
            count=len(reader.pages)
            if count != 1:return False,f'PDF con {count} páginas en vez de 1'
            mediabox=reader.pages[0].mediabox
            if float(mediabox.width)<=0 or float(mediabox.height)<=0:
                return False,'página con dimensiones inválidas'
            return True,f'PDF verificado ({size} bytes, una página)'
        except Exception as exc:
            parser_error=f'{type(exc).__name__}: {exc}'
            try:
                import fitz
                with fitz.open(str(path)) as pdf:
                    if len(pdf)!=1:return False,f'PDF con {len(pdf)} páginas según PyMuPDF'
                    rect=pdf[0].rect
                    if rect.width<=0 or rect.height<=0:
                        return False,'PDF con dimensiones inválidas'
                return True,f'PDF verificado con PyMuPDF ({size} bytes; pypdf: {parser_error})'
            except Exception as exc2:
                return False,f'PDF ilegible ({size} bytes): pypdf={parser_error}; PyMuPDF={type(exc2).__name__}: {exc2}'
    except OSError as exc:
        return False,f'archivo temporal inaccesible: {type(exc).__name__}: {exc}'


def pdf_completo(ruta):
    return estado_pdf_temporal(ruta)[0]


def esperar_pdf_completo(ruta, espera=5.0):
    end=time.monotonic()+max(0,espera)
    while True:
        if pdf_completo(ruta):return True
        if time.monotonic()>=end:return False
        pausa_autocad(min(.20,max(.01,end-time.monotonic())))


'''
PLOT = '''def plotear_con_recuperacion(doc, archivo_temporal, informar, intentos=6):
    """Verifica el PDF y conserva el diagnóstico real de cada intento."""
    base=Path(archivo_temporal)
    ultimo='sin información'
    diagnostico_impresion(f'Inicio de lámina: {base.name}')
    for intento in range(1,intentos+1):
        path=base.with_name(f'{base.stem}_intento_{intento}{base.suffix}')
        enviado=None
        try:
            enviado=doc.Plot.PlotToFile(str(path))
            if esperar_pdf_completo(path,9.0 if enviado else 4.0):
                diagnostico_impresion(f'Intento {intento}: PlotToFile={enviado!r}; PDF correcto')
                return path
            _,detalle=estado_pdf_temporal(path)
            ultimo=f'PlotToFile={enviado!r}; {detalle}'
        except Exception as exc:
            if not es_com_ocupado(exc):
                diagnostico_impresion(f'Intento {intento}: error no recuperable {exc!r}')
                raise
            if esperar_pdf_completo(path,5.0):
                diagnostico_impresion(f'Intento {intento}: COM ocupado; PDF correcto')
                return path
            _,detalle=estado_pdf_temporal(path)
            ultimo=f'COM ocupado ({exc}); {detalle}'
        diagnostico_impresion(f'Intento {intento}/{intentos}: {ultimo}')
        if intento<intentos:
            informar(f'AutoCAD no entregó la hoja; reintento {intento+1}/{intentos}. Revisa si hay diálogos abiertos.')
            pausa_autocad(min(.6*intento,2.5))
    raise RuntimeError(
        f'AutoCAD no pudo generar el PDF tras {intentos} intentos. '
        f'Último resultado: {ultimo}. El diagnóstico está en '
        '%LOCALAPPDATA%\\\\AutomaticCadPDFConverter\\\\diagnostico_impresion.txt')


'''
def patch(path):
    target=Path(path)
    s=target.read_text(encoding='utf-8')
    assert s.count('VERSION = "7.2.6"')==1,'Se esperaba la fuente original 7.2.6'
    s=s.replace('VERSION = "7.2.6"','VERSION = "7.2.7"')
    s=s.replace('Converter v7.2.6.','Converter v7.2.7.')
    start=s.index('def pdf_completo(');end=s.index('def activar_documento(',start)
    s=s[:start]+HEADER+s[end:]
    start=s.index('def plotear_con_recuperacion(');end=s.index('def conectar_autocad(',start)
    s=s[:start]+PLOT+s[end:]
    compile(s,str(target),'exec')
    target.write_text(s,encoding='utf-8')
    print('v7.2.7: validación y diagnóstico integrados')
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('file')
    patch(parser.parse_args().file)
