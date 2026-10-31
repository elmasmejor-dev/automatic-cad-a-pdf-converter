"""Evitar archivos DXF fantasma después de vaciar la lista (v7.2.10)."""
from pathlib import Path
import sys

def once(s, a, b, label):
    n=s.count(a)
    if n!=1: raise RuntimeError(f'{label}: se esperaba una coincidencia, hay {n}')
    return s.replace(a,b,1)

def patch(path):
    path=Path(path)
    s=path.read_text(encoding='utf-8')
    s=once(s,'VERSION = "7.2.9"','VERSION = "7.2.10"','versión')
    s=once(s,'self.archivos=[];self.marcos=[];self.preview_data={};self.preview_pending=set()',
       'self.archivos=[];self.marcos=[];self.preview_data={};self.preview_pending=set()\n        self.generacion_proyecto=0','sesión')
    s=once(s,
       '''        self._set_busy(True);self.progreso.set(0)
        self.fraccion.set(f'0 / {len(self.archivos)}')
        files=self.archivos[:]
        threading.Thread(target=self._worker_detectar,args=(files,),daemon=True).start()

    def _worker_detectar(self,files):''',
       '''        self.generacion_proyecto+=1
        generation=self.generacion_proyecto
        self._set_busy(True);self.progreso.set(0)
        self.fraccion.set(f'0 / {len(self.archivos)}')
        files=self.archivos[:]
        threading.Thread(target=self._worker_detectar,args=(files,generation),daemon=True).start()

    def _worker_detectar(self,files,generation):''','generación detector')
    s=once(s,"self.inbox.put(('detected',frames,errors))","self.inbox.put(('detected',generation,frames,errors))",'resultado detector')
    s=once(s,'def _worker_preview(self,filename,rows):','def _worker_preview(self,filename,rows,generation):','vista previa')
    s=once(s,"self.inbox.put(('preview',filename,data,miniaturas))",
       "self.inbox.put(('preview',generation,filename,data,miniaturas))",'vista previa lista')
    s=once(s,"except Exception as e:self.inbox.put(('preview_failed',filename,str(e)))",
       "except Exception as e:self.inbox.put(('preview_failed',generation,filename,str(e)))",'vista previa fallida')
    start=s.index("            elif kind=='detected':")
    end=s.index("            elif kind=='update_checked':", start)
    s=s[:start]+'''            elif kind=='detected':
                if event[1]!=self.generacion_proyecto:
                    continue
                self.marcos=event[2]
                self.preview_data.clear()
                self.preview_pending.clear()
                self.mapa_miniaturas.clear()
                self.mapa_fotos.clear()
                self.refrescar()
                self.status.set(f'{len(self.marcos)} posibles láminas detectadas. Comprueba la vista previa.')
                self.fraccion.set(f'{len(self.marcos)} hojas')
                self.progreso.set(100);self._set_busy(False)
                if event[3]:messagebox.showwarning('Archivos con problemas','\\n\\n'.join(event[3][:6]))
                frames=defaultdict(list)
                for r in self.marcos:frames[r.archivo].append(r)
                for filename,rows in frames.items():
                    self.preview_pending.add(filename)
                    threading.Thread(target=self._worker_preview,
                                     args=(filename,rows,event[1]),daemon=True).start()
            elif kind=='preview':
                if event[1]!=self.generacion_proyecto:
                    continue
                filename=event[2]
                self.preview_pending.discard(filename)
                visibles={frame for frame in self.marcos if frame.archivo==filename}
                if not visibles:continue
                datos={frame:value for frame,value in event[3].items() if frame in visibles}
                miniaturas={frame:value for frame,value in event[4].items() if frame in visibles}
                self.preview_data[filename]=datos
                self.mapa_miniaturas.update(miniaturas)
                self.mapa_fotos.clear()
                self.dibujar()
                self.dibujar_mapa()
                self.status.set(f'Vista detallada lista: {len(datos)} láminas con dibujo; '
                                f'{len(miniaturas)} miniaturas precalculadas. '
                                'El mapa también dibuja trazos directamente.')
            elif kind=='preview_failed':
                if event[1]!=self.generacion_proyecto:
                    continue
                self.preview_pending.discard(event[2])
                if any(frame.archivo==event[2] for frame in self.marcos):
                    self.status.set('No se pudo crear la vista previa: '+str(event[3]))
                    self.dibujar()
'''+s[end:]
    start=s.index('    def eliminar(self):')
    end=s.index('    def mover(self,direction):',start)
    s=s[:start]+'''    def eliminar(self):
        """Quitar hojas seleccionadas sin incluir archivos ya vacíos."""
        if self.busy:return
        ids={int(i) for i in self.tree.selection()}
        if not ids:return
        self.marcos=[r for k,r in enumerate(self.marcos) if k not in ids]
        restantes=set(self.marcos)
        visibles={r.archivo for r in restantes}
        self.archivos=[p for p in self.archivos if p in visibles]
        for archivo in list(self.preview_data):
            if archivo not in visibles:
                self.preview_data.pop(archivo,None)
            else:
                self.preview_data[archivo]={r:v for r,v in self.preview_data[archivo].items() if r in restantes}
        self.mapa_miniaturas={r:v for r,v in self.mapa_miniaturas.items() if r in restantes}
        self.mapa_fotos.clear()
        self.refrescar(select=min(ids))
        self.status.set(f'Quedan {len(self.marcos)} láminas en la lista de exportación.')

    def vaciar_laminas(self):
        """Vaciar láminas, archivos y cachés de la sesión sin borrar DXF del disco."""
        if self.busy or not (self.marcos or self.archivos):return
        hojas=len(self.marcos)
        proyectos=len(self.archivos)
        if not messagebox.askyesno('Vaciar lista y archivos',
             f'¿Quitar las {hojas} láminas y descargar los {proyectos} archivos DXF de la sesión?\\n\\n'
             'Los archivos originales del disco NO se borrarán.'):
            return
        self.generacion_proyecto+=1
        self.archivos.clear()
        self.marcos.clear()
        self.preview_data.clear()
        self.preview_pending.clear()
        self.mapa_miniaturas.clear()
        self.mapa_fotos.clear()
        self.mapa_image_refs.clear()
        self.mapa_hover_indice=None
        self.mapa_rectangulos.clear()
        self.mapa_drag_inicio=self.mapa_drag_actual=None
        self.seleccion.set('todas')
        self.rango.set('')
        self.refrescar()
        self.fraccion.set('0 / 0')
        self.progreso.set(0)
        self.status.set('Lista y archivos descargados. Agrega el DXF que quieras exportar.')
        self._update_export_button()

'''+s[end:]
    compile(s,str(path),'exec')
    path.write_text(s,encoding='utf-8')
    print('v7.2.10: fuentes DXF, vistas previas y exportación sincronizadas')
if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit('Uso: patch_stable_7210.py ARCHIVO_PY')
    patch(sys.argv[1])
