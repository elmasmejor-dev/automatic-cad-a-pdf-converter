# Automatic CAD a PDF Converter v7.2.1 🍪

## Novedad principal

**Nombres de PDF basados en el DXF original.** Al guardar un PDF conjunto, la aplicación propone el nombre del archivo de origen en lugar del nombre genérico:

- `Plano estructura.dxf` → `Plano estructura.pdf`
- `PARTE COMUN peñon(1).dxf` → `PARTE COMUN peñon(1).pdf`
- Al unir dibujos distintos, el nombre sugerido identifica el primero y la cantidad restante.
- Los PDF separados siguen usando nombres numerados por lámina.
- El usuario puede modificar libremente el nombre y la ubicación al guardar.

## Funciones conservadas

- Detector de láminas DXF y vista previa clásica.
- Mapa de láminas interactivo, selección con el mouse y pantalla completa.
- Papel automático y manual A0–A4.
- Exportación de PDF único o individual, con motor AutoCAD.
- Modo de impresión que evita abrir cada PDF en el visor.
- Búsqueda e instalación opcional de actualizaciones a través de GitHub.

## Archivo de publicación

**Etiqueta:** `v7.2.1`

**Nombre del instalador:** `Setup_Automatic_CAD_a_PDF_Converter_v7_2_1.exe`

**SHA-256 comprobado del instalador preparado:**

```text
26332a7407cb2f8575b62bca5d9f332ad0b9d4c480840f3d480384c52c0d067b
```

## Estado de comprobación

El instalador corresponde a un ejecutable PE de Windows de 64 bits, y el código integrado indica la versión 7.2.1. La mejora del nombre sugerido pasó las pruebas realizadas anteriormente. Sigue siendo necesario verificar la instalación y exportación de esta versión en Windows real antes de considerarla plenamente validada.

> Esta versión mantiene el instalador que prepara Python en la carpeta de la aplicación; el instalador autónomo propuesto en v7.3 no forma parte de esta publicación.

## Publicar la actualización

1. Abre https://github.com/elmasmejor-dev/automatic-cad-a-pdf-converter/releases/new.
2. Elige **Create new tag**: `v7.2.1`, basado en `main`.
3. Título: `Automatic CAD a PDF Converter v7.2.1`.
4. Adjunta el instalador con el nombre exacto indicado arriba.
5. Antes de publicar, comprueba que el SHA-256 del archivo que subiste coincida con el de esta nota.
6. Publica como una versión estable (sin marcar **Pre-release**).

La app v7.2.0 debería detectar la versión superior al iniciarse cuando la publicación esté visible en `releases/latest`.
