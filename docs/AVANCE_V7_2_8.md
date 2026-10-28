# Desarrollo v7.2.8 — seguridad y estabilidad 🍪

**Estado:** en desarrollo, todavía no publicada.

La última versión estable recomendada sigue siendo la **v7.2.7**, que ya fue probada en Windows. Se creó esta rama para organizar la revisión sin publicar una actualización a los usuarios.

## Correcciones implementadas y probadas localmente

- El motor PDF independiente valida **todas** las páginas antes de publicar un PDF. Si alguna falla, conserva el archivo existente sin sobrescribirlo.
- La salida de PDFs individuales se prepara antes de publicar los archivos y revierte los archivos generados cuando ocurre un fallo durante la publicación.
- El actualizador comprueba coincidencia entre la etiqueta de GitHub, el nombre del instalador y la URL, además del SHA-256.
- Snapshot/restauración de parámetros del trazador y Layout activo de AutoCAD, con avisos cuando alguna propiedad no se pudo restaurar.
- Prototipo aislado para transformar una **copia temporal** de DWG a DXF 2018 mediante AutoCAD ActiveX (todavía no integrado en la interfaz).

**Resultados:** 10 tests locales exitosos, detector verificado con 83 marcos en el DXF de referencia y una exportación A3 de muestra válida.

## Antes de publicar

- Compilar y ejecutar el instalador en Windows.
- Probar el trazador real en AutoCAD 2026 y la restauración de configuración.
- Evaluar referencias externas (XREF), objetos proxy y fuentes al convertir DWG.
- Incorporar límites de recursos y cancelación segura.
- Revisar dependencia y firma del instalador.

## Código fuente

Por ahora **no se ha subido código fuente de la aplicación a este repositorio público**. Los cambios se prepararon en un paquete de desarrollo para uso privado y pruebas. No se realizará ninguna publicación automática en Releases sin comprobar el instalador.

## Compatibilidad DWG prevista

El primer método usa AutoCAD sobre una copia temporal, no sobre el DWG original. Autodesk documenta que `Document.SaveAs` cambia el nombre del documento activo; por eso la copia de trabajo es esencial.

El método opcional sin AutoCAD requerirá revisar previamente las condiciones de uso y distribución de ODA File Converter.
