"""Validated, atomic PDF replacement for both export engines."""
from pathlib import Path
import errno, os, time
from pypdf import PdfReader

def publicar_pdf_atomico(temporal, destino, paginas, reintentos=4, pausa=.35):
    temp, output=Path(temporal),Path(destino)
    if output.is_dir():
        raise IsADirectoryError(f'La ruta de salida es una carpeta: {output}')
    if not temp.is_file() or temp.stat().st_size<100:
        raise RuntimeError('El archivo PDF temporal no existe o está vacío')
    if temp.absolute()==output.absolute():
        raise ValueError('La ruta temporal y la final coinciden')
    size=temp.stat().st_size
    with temp.open('rb') as f:
        if not f.read(1024).startswith(b'%PDF-'):
            raise RuntimeError('El PDF final no tiene cabecera PDF')
        f.seek(max(0,size-4096))
        if b'%%EOF' not in f.read():
            raise RuntimeError('El PDF final está truncado')
        f.seek(0)
        reader=PdfReader(f,strict=False)
        if len(reader.pages)!=paginas:
            raise RuntimeError(f'El PDF tiene {len(reader.pages)} páginas, en lugar de {paginas}. El anterior permanece intacto.')
        for page in reader.pages:
            if float(page.mediabox.width)<=0 or float(page.mediabox.height)<=0:
                raise RuntimeError('Una página del PDF final tiene dimensiones inválidas')
    for intento in range(max(1,reintentos)):
        try:
            os.replace(temp,output)
            return output
        except OSError as exc:
            locked=(getattr(exc,'winerror',None) in (5,32,33) or
                    exc.errno in (errno.EACCES,errno.EPERM,errno.EBUSY))
            if not locked:
                raise RuntimeError(f'No se pudo guardar el PDF: {exc}') from exc
            if intento+1 < max(1,reintentos):
                time.sleep(pausa)
            else:
                raise PermissionError(
                    f'No se pudo sobrescribir «{output.name}». Cierra el PDF '
                    'en Adobe Reader, Edge u otros visores, revisa los permisos '
                    'y vuelve a exportar. El PDF anterior permanece intacto.') from exc
