# Automatic CAD a PDF Converter v7.2.3 🍪

## Corrección de exportación con AutoCAD

Esta versión mejora la resistencia ante el error COM **-2147418111 (RPC_E_CALL_REJECTED)**, que puede aparecer cuando AutoCAD está ocupado y rechaza temporalmente una llamada de automatización.

### Cambios

- **Reintentos automáticos** cuando AutoCAD rechaza temporalmente una llamada.
- Comprueba que el documento correcto esté activo y configura el trazado en primer plano.
- **Verifica las páginas temporales** antes de ensamblar el archivo final.
- Si AutoCAD imprimió una página pero devolvió un error, intenta reconocer el resultado para **evitar duplicados**.
- **Protección de resultados:** si una lámina falla definitivamente, no reemplaza el PDF final por uno incompleto y conserva el archivo anterior.
- Mantiene la vista previa clásica, mapa interactivo, papeles A0–A4, selección de páginas, impresión silenciosa y nombres basados en el DXF.

### Pruebas realizadas

- 26 pruebas automatizadas, incluidas situaciones simuladas de fallos transitorios, permanentes y PDF temporal inválido.
- Detección de 83 láminas en el DXF de referencia.
- Se comprobó que el instalador generado corresponde a Windows de 64 bits.

**Limitación:** todavía falta validar la exportación completa con AutoCAD 2026 en un equipo Windows real. Esta corrección reduce el riesgo de fallos, pero no garantiza que AutoCAD nunca rechace una operación.

## Instalador

- **Etiqueta para GitHub:** `v7.2.3`
- **Nombre de archivo:** `Setup_Automatic_CAD_a_PDF_Converter_v7_2_3.exe`
- **SHA-256 calculado del instalador:**

```text
d595b1ab017fe7b07fb69a07c5933c02946d627d65b7fb826d9414d460c35166
```

El instalador sigue preparando Python y las bibliotecas en la carpeta de la aplicación cuando es necesario. No es el empaquetado autónomo experimental de la v7.3.

## Instrucciones de publicación

1. Abre https://github.com/elmasmejor-dev/automatic-cad-a-pdf-converter/releases/new.
2. Crea el tag `v7.2.3` desde `main`.
3. Pon como título **Automatic CAD a PDF Converter v7.2.3**.
4. Adjunta el ejecutable `Setup_Automatic_CAD_a_PDF_Converter_v7_2_3.exe`.
5. Comprueba la huella SHA-256 del archivo adjunto.
6. Publica la release como estable, sin marcar *Pre-release*, para que el programa pueda reconocerla desde `releases/latest`.

**Nota:** las notas están en el repositorio, pero adjuntar el ejecutable y publicar la release debe hacerse manualmente desde GitHub.
