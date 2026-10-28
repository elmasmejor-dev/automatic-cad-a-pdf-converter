# Publicar actualizaciones

## 1. Preparar el instalador

- Compila y **prueba en Windows** una nueva versión del programa.
- Usa un número de versión creciente, por ejemplo `7.1.0`, y mantenlo igual en el programa, el instalador y la publicación.
- Asegúrate de que el instalador conserva las preferencias del usuario y permite actualizar la instalación existente.
- Si es posible, firma digitalmente el instalador.

## 2. Crear una publicación en GitHub

1. Abre https://github.com/elmasmejor-dev/automatic-cad-a-pdf-converter/releases/new
2. Crea una etiqueta, por ejemplo `v7.1.0`.
3. Escribe el título **Automatic CAD a PDF Converter v7.1.0**.
4. Describe los cambios y errores corregidos.
5. Adjunta el archivo instalador `.exe` (no el código fuente).
6. Publica la release como estable si la has probado. No la marques como *prerelease* si esperas que aparezca en `releases/latest`.

## 3. Comprobación

Esta dirección debe responder con los datos de la versión publicada:

https://api.github.com/repos/elmasmejor-dev/automatic-cad-a-pdf-converter/releases/latest

El actualizador del programa debe comparar `tag_name` con la versión local, localizar el instalador entre `assets`, mostrar los cambios y **preguntar antes de instalar**.

## 4. Recomendaciones de seguridad

- Descargar exclusivamente por HTTPS desde GitHub.
- Comprobar el código HTTP y que el archivo descargado no esté vacío.
- Verificar SHA-256 contra una suma publicada de confianza; preferiblemente, verificar también la firma digital del instalador.
- Descargar a un archivo temporal, verificarlo y solo entonces ejecutar el instalador.
- Cerrar la aplicación antes de instalar, conservar la configuración y permitir cancelar.
- Si la conexión falla, iniciar la aplicación normalmente.
- Para evitar interrupciones, realizar la consulta en segundo plano sin bloquear la interfaz.

**Nota:** documentar este procedimiento no activa por sí solo el actualizador. La función debe integrarse y probarse en una versión futura de Automatic CAD a PDF Converter.