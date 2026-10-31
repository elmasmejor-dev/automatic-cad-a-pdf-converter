# Automatic CAD a PDF Converter v7.2.10 🍪

## Actualización estable

Esta versión actualiza el conversor DXF estable de la serie 7.2. La aplicación conserva la interfaz, los motores de exportación y Python 3.12 integrado.

### Correcciones

- **Vaciar lista** elimina todas las láminas, los archivos DXF cargados y sus cachés de vista previa **de la sesión**. No borra los DXF del disco.
- Al cargar otro DXF después de vaciar la lista, solo se detecta y exporta el nuevo proyecto. Ya no se mezclan archivos de sesiones anteriores.
- **Quitar** sigue permitiendo eliminar láminas individualmente o varias seleccionadas, y descarga el DXF cuando se elimina su última hoja.
- Las tareas de detección y miniaturas anteriores se descartan si pertenecen a otra sesión.
- Se conservan las mejoras de la v7.2.9 para **sobrescribir PDFs de manera segura**, informar de archivos bloqueados y evitar resultados parciales.
- Python y bibliotecas permanecen integrados: no hace falta instalar Python aparte.

### Compatibilidad

- Windows 10 y 11 de 64 bits.
- Para la impresión de máxima fidelidad se necesita AutoCAD.
- La integración DWG sigue en **beta separada** y NO forma parte de esta versión DXF estable.

### Instalación y actualización

El instalador oficial `Setup_Automatic_CAD_a_PDF_Converter_v7_2_10.exe` conserva el identificador de instalación, la ubicación y los accesos directos de la v7.2.7 estable. Permite actualizar la instalación estable anterior.

El instalador de prueba `7.2.10 PRUEBA` se instalaba por separado; si también está presente, puede desinstalarse después de verificar la versión estable.

### Validación

La corrección fue probada en Windows por el desarrollador antes de aprobar la publicación. La compilación oficial se ejecuta en GitHub Actions con comprobaciones de integridad y de creación del ejecutable. Los casos específicos de cada versión y configuración de AutoCAD pueden variar.

**Creado por Manu · Hecho con GPT**
