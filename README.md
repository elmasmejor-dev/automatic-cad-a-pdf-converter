# 🍪 Automatic CAD a PDF Converter

Aplicación para Windows que detecta automáticamente láminas de archivos **DXF** y las convierte a PDF.

> **Creado por Manu · Hecho con GPT**

## Funciones

- Detección automática de marcos de láminas.
- Visor clásico y mapa interactivo de láminas, con selección por clic o arrastre.
- Vista de mapa a pantalla completa con detalles de los planos.
- Exportación de una o varias hojas, en un PDF único o en PDF separados.
- Selección manual o detección automática de papel A0–A4.
- Motor AutoCAD de máxima fidelidad y motor independiente experimental.
- Barra de progreso y opción para evitar que los archivos se abran en un visor externo.
- **Desde la versión 7.1.0:** búsqueda de actualizaciones al iniciar y botón para comprobarlas manualmente.

## Descargar

Los instaladores oficiales estarán publicados en **[GitHub Releases](https://github.com/elmasmejor-dev/automatic-cad-a-pdf-converter/releases)**.

La versión estable publicada más reciente se encuentra en la página de Releases. Descarga únicamente los instaladores adjuntos a publicaciones oficiales.

**Requisitos:** Windows 10/11 de 64 bits. El instalador prepara Python y las bibliotecas en la carpeta de la aplicación; para exportar con máxima fidelidad es necesario tener AutoCAD instalado.

## Actualizaciones

El programa consulta esta dirección de GitHub:

```text
https://api.github.com/repos/elmasmejor-dev/automatic-cad-a-pdf-converter/releases/latest
```

Cuando hay una versión estable más reciente, presenta las novedades y pregunta si deseas descargar e instalar. No instala nada sin confirmación. Comprueba además el SHA-256 informado por GitHub antes de ejecutar el archivo descargado.

Si no hay conexión, o todavía no hay una versión publicada, el programa continúa funcionando normalmente.

La versión **7.0.1 y anteriores no tienen actualizador**, por lo que la transición a 7.1.0 requiere instalar el nuevo programa una vez de forma manual.

## Para el desarrollador

- [Guía para publicar versiones e instaladores](docs/PUBLICAR_ACTUALIZACIONES.md)
- [Notas de la versión 7.1.0](docs/NOTAS_V7_1_0.md)

El repositorio es un canal de documentación y distribución. No es necesario publicar el código fuente del programa para distribuir las versiones instalables.

## Versión 7.2.3 preparada para publicar

La versión **7.2.3** mejora la exportación a PDF cuando AutoCAD rechaza temporalmente llamadas de automatización. Consulta las [notas de la versión 7.2.3](docs/NOTAS_V7_2_3.md).

**Estado:** documentación preparada; el instalador todavía debe adjuntarse y publicarse en GitHub Releases. La última versión publicada actualmente es la v7.2.2.
