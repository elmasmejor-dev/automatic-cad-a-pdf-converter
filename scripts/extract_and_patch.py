"""Recover the tested DXF application from the original public Windows installer.
Checks the official installer checksum and the source patch before building.
"""
import argparse, hashlib, json, sys
from pathlib import Path
from io import BytesIO
from zipfile import ZipFile

BASE_SHA256 = "0f084b3520903f0f7ab678c3f9055c60088077fcadc2130dcf42addde042e103"
REQUIRED = ("automatic_cad_to_pdf.py","update_manager.py","dxfless_renderer.py",
            "galleta.png","galleta_ui.png","galleta.ico","AutomaticCadUpdateHelper.exe")

def digest(b):
    return hashlib.sha256(b).hexdigest()

def extract(blob):
    e=blob.rfind(b"PK\x05\x06")
    i=blob.find(b"PK\x03\x04")
    if e<0 or i<0: raise ValueError("ZIP interno no encontrado")
    comment=int.from_bytes(blob[e+20:e+22],"little")
    with ZipFile(BytesIO(blob[i:e+22+comment])) as z:
        return {name:z.read(name) for name in REQUIRED}

def apply(base, spec):
    if digest(base.encode()) != spec["sha256_before"]:
        raise ValueError("Versión de origen distinta: "+str(spec["sha256_before"]))
    lines=base.splitlines(keepends=True)
    out=[]
    last=0
    for edit in spec["edits"]:
        start,stop=edit["start"],edit["stop"]
        if not (0<=last<=start<=stop<=len(lines)): raise ValueError("Parche inválido")
        out.extend(lines[last:start])
        out.append(edit["replacement"])
        last=stop
    out.extend(lines[last:])
    result="".join(out)
    if digest(result.encode()) != spec["sha256_after"]:
        raise ValueError("El código corregido no superó la verificación SHA-256")
    return result

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--installer",required=True)
    ap.add_argument("--out",default="app-src")
    opts=ap.parse_args()
    blob=Path(opts.installer).read_bytes()
    if digest(blob)!=BASE_SHA256:
        raise ValueError("El instalador base no corresponde a la versión 7.2.2 verificada")
    files=extract(blob)
    from base64 import b64decode
    import zlib
    packed=Path(__file__).with_name("source_patch.txt").read_text().strip()
    patches=json.loads(zlib.decompress(b64decode(packed)))
    for name,spec in patches["files"].items():
        target=apply(files[name].decode("utf-8-sig"),spec)
        target=target.replace("7.2.5","7.2.6")
        if name=="update_manager.py":
            old="app_dir = Path(app_dir or Path(__file__).resolve().parent).resolve()"
            new="app_dir = Path(app_dir or (Path(sys.executable).resolve().parent if getattr(sys, 'frozen', False) else Path(__file__).resolve().parent)).resolve()"
            if target.count(old)!=1: raise ValueError("No se pudo reparar el actualizador del EXE independiente")
            target=target.replace(old,new)
        files[name]=target.encode()
    dst=Path(opts.out)
    dst.mkdir(parents=True,exist_ok=True)
    for name,b in files.items(): (dst/name).write_bytes(b)
    for name in ("automatic_cad_to_pdf.py","update_manager.py","dxfless_renderer.py"):
        compile((dst/name).read_text(encoding="utf-8"),str(dst/name),"exec")
    assert 'VERSION = "7.2.6"' in (dst/"automatic_cad_to_pdf.py").read_text(encoding="utf-8")
    print("Código comprobado de v7.2.6 recuperado",len(files),"archivos")

if __name__=="__main__":
    main()
