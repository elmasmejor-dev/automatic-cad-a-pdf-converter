"""Patch ONLY the stable DXF v7.2.7 application; do not include DWG beta."""
from pathlib import Path
import argparse

RENDER_HELPER = '''
def publicar_paginas_seguras(marcos, parts, output, modo):
    """Check ALL sheets before publishing, and roll back new individual PDFs."""
    from pypdf import PdfReader, PdfWriter
    from automatic_cad_to_pdf import _sanitize_filename, _unique_file
    from pdf_safety import publicar_pdf_atomico
    import shutil
    output=Path(output)
    if len(parts)!=len(marcos) or any(i not in parts for i in range(len(marcos))):
        raise RuntimeError('Faltan páginas; no se modificó el PDF anterior')
    for i in range(len(marcos)):
        with Path(parts[i]).open('rb') as f:
            if len(PdfReader(f,strict=False).pages)!=1:
                raise RuntimeError(f'La página {i+1} es inválida')
    if modo=='unico':
        output.parent.mkdir(parents=True,exist_ok=True)
        writer=PdfWriter()
        fd,stage=tempfile.mkstemp(prefix='.cad_pdf_',suffix='.pdf',dir=str(output.parent))
        os.close(fd)
        try:
            for i in range(len(marcos)):
                writer.append(str(parts[i]))
            with open(stage,'wb') as f:
                writer.write(f)
                f.flush()
                os.fsync(f.fileno())
            publicar_pdf_atomico(stage,output,len(marcos))
            return len(marcos),[],[str(output)]
        finally:
            writer.close()
            Path(stage).unlink(missing_ok=True)
    if modo!='separado':raise ValueError('Modo de exportación desconocido')
    output.mkdir(parents=True,exist_ok=True)
    reserved=set();staged=[];published=[];plan=[]
    try:
        for i,frame in enumerate(marcos):
            filename=f'{_sanitize_filename(Path(frame.archivo).stem)}_lamina_{i+1:03d}.pdf'
            dest=_unique_file(output/filename,reserved)
            fd,tmp=tempfile.mkstemp(prefix='.cad_stage_',suffix='.tmp',dir=str(output))
            os.close(fd)
            stage=Path(tmp);staged.append(stage)
            with Path(parts[i]).open('rb') as source,stage.open('wb') as target:
                shutil.copyfileobj(source,target)
                target.flush();os.fsync(target.fileno())
            if stage.stat().st_size!=Path(parts[i]).stat().st_size:
                raise RuntimeError('Copia temporal de página incompleta')
            plan.append((stage,dest))
        for stage,dest in plan:
            with dest.open('xb') as target,stage.open('rb') as source:
                published.append(dest)
                shutil.copyfileobj(source,target)
                target.flush();os.fsync(target.fileno())
            if dest.stat().st_size!=stage.stat().st_size:
                raise RuntimeError('PDF individual incompleto')
        return len(marcos),[],[str(dst) for _,dst in plan]
    except Exception:
        for file in published:
            try:file.unlink()
            except OSError:pass
        raise
    finally:
        for file in staged:file.unlink(missing_ok=True)
'''

def replace_once(source,old,new,description):
    if source.count(old)!=1:
        raise RuntimeError(f'Código base cambiado: {description}: {source.count(old)} coincidencias')
    return source.replace(old,new,1)

def patch(folder):
    folder=Path(folder)
    app=folder/'automatic_cad_to_pdf.py'
    s=app.read_text(encoding='utf-8')
    s=replace_once(s,'VERSION = "7.2.7"','VERSION = "7.2.9"','version')
    s=replace_once(s,"        self.btn_eliminar.pack(side='left',padx=(0,8))",
      "        self.btn_eliminar.pack(side='left',padx=(0,5))\n"
      "        self.btn_vaciar=self._boton(tools,'Vaciar lista',self.vaciar_laminas)\n"
      "        self.btn_vaciar.pack(side='left',padx=(0,8))",'botón')
    vaciar="""    def vaciar_laminas(self):
        if self.busy or not self.marcos:return
        total=len(self.marcos)
        if not messagebox.askyesno('Vaciar lista de láminas',
                f'¿Quitar las {total} láminas de la lista?\\n\\n'
                'Los DXF originales no se eliminarán. Puedes volver a detectarlos.'):
            return
        self.marcos.clear()
        self.mapa_miniaturas.clear()
        self.mapa_fotos.clear()
        self.preview_data.clear()
        self.refrescar()
        self.fraccion.set('0 láminas')
        self.progreso.set(0)
        self.status.set('Lista vaciada. Los archivos DXF siguen cargados.')
        self._update_export_button()

"""
    s=replace_once(s,'    def mover(self,direction):',vaciar+'    def mover(self,direction):','método vaciar')
    s=replace_once(s,'self.btn_eliminar,self.btn_subir,self.btn_bajar,self.btn_visor',
       'self.btn_eliminar,self.btn_vaciar,self.btn_subir,self.btn_bajar,self.btn_visor','estado ocupado')
    old="""                    final_reader=PdfReader(out_temp,strict=True)
                    if len(final_reader.pages)!=len(marcos):
                        raise RuntimeError('El PDF final no contiene todas las páginas solicitadas')
                    os.replace(out_temp,output)"""
    s=replace_once(s,old,
      "                    from pdf_safety import publicar_pdf_atomico\n"
      "                    publicar_pdf_atomico(out_temp,output,len(marcos))",'reemplazo PDF AutoCAD')
    s=replace_once(s,"'El archivo ya existe. ¿Quieres reemplazarlo?'",
         "'El archivo ya existe. ¿Quieres reemplazarlo?\\n\\nCierra el visor PDF antes de continuar si tienes abierto este archivo.'",
         'confirmación de sobrescritura')
    compile(s,str(app),'exec')
    app.write_text(s,encoding='utf-8')
    renderer=folder/'dxfless_renderer.py'
    s=renderer.read_text(encoding='utf-8')
    first=s.index("                    if modo=='unico':parts[index]=part")
    last=s.index("                except Exception as e:",first)
    s=s[:first]+"                    parts[index]=part\n"+s[last:]
    first=s.index("        if modo=='unico' and parts:")
    s=s[:first]+"""        if errors or len(parts)!=len(marcos):
            raise RuntimeError('No se guardó ningún PDF: faltan páginas. '
                               + '\\n'.join(errors[:8]))
        informar('Verificando y publicando todas las páginas…')
        return publicar_paginas_seguras(marcos,parts,output,modo)

"""
    s=s.replace('errors=[]; parts={}; generated=[];reserved=set();done=0',
                'errors=[]; parts={};done=0',1)
    s+='\n'+RENDER_HELPER
    compile(s,str(renderer),'exec')
    renderer.write_text(s,encoding='utf-8')
    print('Stable DXF v7.2.9 patched: clear all sheets, safe PDF overwrite, no partial PDF')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('source_folder')
    patch(parser.parse_args().source_folder)
