# Publicación de versiones en GitHub Releases

La aplicación **7.1.0** ya incluye el comprobador de actualizaciones. Para activarlo entre usuarios, debes publicar la primera versión de forma manual en Releases.

## Publicar la versión inicial

1. Abre https://github.com/elmasmejor-dev/automatic-cad-a-pdf-converter/releases/new
2. En **Choose a tag**, crea `v7.1.0` a partir de `main`.
3. Título: `Automatic CAD a PDF Converter v7.1.0`.
4. Agrega un resumen de novedades (puedes usar [estas notas](NOTAS_V7_1_0.md)).
5. Arrastra al área **Attach binaries** exactamente este instalador de Windows:
   `Setup_Automatic_CAD_a_PDF_Converter_v7_1_0.exe`
6. No marques **Set as a pre-release** ni **Save draft** si quieres que aparezca en la API `releases/latest`.
7. Selecciona **Publish release**.

**Importante:** el instalador se obtiene de la compilación local verificada. No se ha publicado el archivo EXE en este repositorio mediante la conexión actual; hay que adjuntarlo manualmente.

## Cómo publicar una actualización posterior

1. Genera una nueva versión, por ejemplo `7.2.0`, con su instalador:
   `Setup_Automatic_CAD_a_PDF_Converter_v7_2_0.exe`.
2. Comprueba el instalador en Windows antes de compartirlo.
3. Crea una nueva publicación estable de GitHub con etiqueta `v7.2.0` y sube su `.exe`.
4. La app que tenga 7.1.0 detectará 7.2.0 al iniciarse y mostrará las novedades.
5. La descarga se hace a través de HTTPS y se valida con el SHA-256 (`digest`) de la API de GitHub.

## Reglas de compatibilidad con el actualizador

- El **tag** debe ser `vN.N.N`, por ejemplo `v7.2.0`.
- El archivo debe llamarse `Setup_Automatic_CAD_a_PDF_Converter_vN_N_N.exe`.
- Debe ser una **release estable** (ni borrador ni prerelease).
- GitHub genera automáticamente un SHA-256 para los assets publicados.
- El instalador debe conservar la carpeta instalada y los ajustes del usuario.
- El actualizador solicita confirmación antes de descargar y también antes de ejecutar.

## Cómo comprobarlo

API de última versión:
https://api.github.com/repos/elmasmejor-dev/automatic-cad-a-pdf-converter/releases/latest

Página de publicaciones:
https://github.com/elmasmejor-dev/automatic-cad-a-pdf-converter/releases

Para probar una actualización de verdad, instala una versión anterior que contenga el actualizador y publica después una versión superior. La 7.0.1 no detecta actualizaciones automáticamente.

Firma digitalmente el instalador si vas a distribuirlo ampliamente, además de verificar su integridad con SHA-256.


## Ensayo de la actualización 7.1 → 7.2

- [Notas y comprobaciones de la versión 7.2.0](NOTAS_V7_2_0.md).
- Publica un Release estable con tag `v7.2.0`, adjuntando el archivo `Setup_Automatic_CAD_a_PDF_Converter_v7_2_0.exe`.
- Abre la app **7.1.0 instalada** para probar la detección antes de instalar el archivo manualmente.
- La aplicación 7.1.0 cierra su ventana tras iniciar el instalador; la instalación 7.2.0 espera a que el programa termine de cerrarse antes de sustituir los archivos.
- A partir de la aplicación 7.2.0, un ayudante nativo espera directamente al cierre de Python antes de iniciar posteriores instaladores.
