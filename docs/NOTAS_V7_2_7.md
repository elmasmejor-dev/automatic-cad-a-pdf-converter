# Automatic CAD a PDF Converter v7.2.7 🍪

## Novedades

**Corrección de impresión de PDF con AutoCAD y mejor diagnóstico.**

- Validación más tolerante de archivos PDF de una página generados por AutoCAD, sin aceptar archivos incompletos.
- Recuperación de PDFs que algunos lectores estrictos consideran irregulares.
- Registro detallado de intentos de impresión cuando AutoCAD no genera un archivo o rechaza una llamada.
- Se mantienen los reintentos de comunicación con AutoCAD y la protección para no sobrescribir un PDF anterior si una hoja falla.
- **Python 3.12 y bibliotecas incluidos dentro del instalador**: ya no hace falta instalar Python por separado.
- Se conservan la detección DXF, las vistas previas, el mapa de láminas, la selección de páginas, papel A0–A4 y nombres de salida basados en el DXF.

## Requisitos

Windows 10/11 de 64 bits. AutoCAD es necesario para utilizar el motor de impresión de máxima fidelidad. La instalación de la aplicación no requiere instalar Python por separado.

## Verificación

- El paquete fue compilado en GitHub Actions en Windows.
- Se verificó su integridad y que contiene Python empaquetado.
- El instalador ha sido **probado con éxito en un computador del desarrollador**, incluida la exportación que fallaba previamente.
- No se garantiza que todos los dibujos y todas las configuraciones de AutoCAD funcionen sin excepciones.

## Instalador

Archivo oficial: `Setup_Automatic_CAD_a_PDF_Converter_v7_2_7.exe`

SHA-256 de la compilación que se probó y se publicará:

```text
09d0ab449d5e16926ef85e55d7fd6720f9256828c859d39be043abf9d9e475c6
```

**Creado por Manu · Hecho con GPT**
