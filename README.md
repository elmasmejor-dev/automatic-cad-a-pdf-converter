# 🍪 Automatic CAD a PDF Converter

Aplicación para Windows que detecta láminas en dibujos **DXF** y facilita su exportación a PDF.

> **Creado por Manu · Hecho con GPT**

## Funciones principales

- Detección automática de marcos de láminas en archivos DXF.
- Vista previa de cada lámina y mapa interactivo (beta) para localizarlas y seleccionarlas.
- Selección por páginas, rangos o grupos desde el mapa.
- Exportación de todas las láminas a un solo PDF o a archivos PDF individuales.
- Tamaños de papel A0, A1, A2, A3 y A4: detección automática o selección manual.
- Barra de progreso y opción para evitar que se abra el visor PDF durante cada conversión.
- Impresión con motor de AutoCAD para mayor fidelidad; el modo independiente es experimental.

## Descargar e instalar

Las versiones públicas se distribuirán desde **[Releases](https://github.com/elmasmejor-dev/automatic-cad-a-pdf-converter/releases)**. Todavía no se ha publicado una versión en esa sección.

Cuando haya una publicación, abre la versión más reciente, descarga el instalador `.exe` y sigue el asistente.

**Requisitos:** Windows 10/11 de 64 bits. Para imprimir mediante el motor de AutoCAD, es necesario tener AutoCAD instalado. El instalador del programa incluye la configuración de su propio entorno Python.

## Actualizaciones

Está previsto que la aplicación consulte la publicación más reciente al iniciarse y **pregunte al usuario** antes de descargar e instalar una actualización. Las actualizaciones no se instalarán sin su consentimiento.

La dirección del servicio de versiones es:

```text
https://api.github.com/repos/elmasmejor-dev/automatic-cad-a-pdf-converter/releases/latest
```

Este repositorio es el canal de **distribución y documentación**. No es necesario publicar aquí el código fuente de la aplicación.

Consulta [cómo publicar una actualización](docs/PUBLICAR_ACTUALIZACIONES.md).
