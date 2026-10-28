# Automatic CAD a PDF Converter v7.2.2 🍪

## Cambios de esta versión

- **Interfaz adaptada a portátiles y pantallas pequeñas**, especialmente 14 pulgadas (1366 × 768).
- La lista de láminas y la vista previa clásica disponen de mucho más espacio vertical.
- **Opciones de exportación desplegables:** puedes ocultarlas para dar prioridad al visor y volver a mostrarlas cuando quieras.
- El botón **Exportar PDF** y la barra de progreso permanecen accesibles.
- Ajuste de tamaño inicial de la ventana según la resolución de pantalla.
- Texto de versión actualizado a **7.2.2** en el título y dentro de la aplicación.

## Funciones que se mantienen

- Detección automática de láminas desde archivos DXF.
- Visor clásico y mapa interactivo (beta), con selección por grupos y vista a pantalla completa.
- Selección de páginas, exportación conjunta o por lámina.
- Papel automático o manual A0, A1, A2, A3 y A4.
- Motor AutoCAD para mayor fidelidad y alternativa independiente experimental.
- Opción de no abrir PDF en Acrobat durante la impresión.
- Sugerencia de nombres de PDF basados en el nombre del DXF.
- Comprobación de actualizaciones desde GitHub Releases con consentimiento antes de instalar.

## Instalador para Windows

**Etiqueta:** `v7.2.2`  
**Nombre del asset:** `Setup_Automatic_CAD_a_PDF_Converter_v7_2_2.exe`  
**Tamaño del archivo:** 3.676.672 bytes

**SHA-256 del instalador:**

```text
0f084b3520903f0f7ab678c3f9055c60088077fcadc2130dcf42addde042e103
```

El archivo es un ejecutable PE de 64 bits para Windows. Conserva el asistente de instalación con preparación de Python y dependencias cuando es necesario; **no** incluye la instalación totalmente autónoma experimental de la v7.3.

## Verificación y límites

La v7.2.2 pasó las comprobaciones de la interfaz en 1366 × 768 y 1280 × 720, las pruebas de regresión previas y la detección de 83 láminas del proyecto Peñón.

La instalación y la impresión real mediante AutoCAD 2026 todavía necesitan confirmación en un equipo Windows.

## Publicar en GitHub

1. Abre https://github.com/elmasmejor-dev/automatic-cad-a-pdf-converter/releases/new
2. Crea el tag `v7.2.2` a partir de la rama `main`.
3. Usa el título **Automatic CAD a PDF Converter v7.2.2**.
4. Adjunta el instalador cuyo nombre se indica arriba.
5. Antes de publicar comprueba el SHA-256.
6. Publica como versión estable (sin marcar *Pre-release*).

La publicación deberá aparecer en `releases/latest` para que el actualizador de las versiones anteriores pueda detectarla.
