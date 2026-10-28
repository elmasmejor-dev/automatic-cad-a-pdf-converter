# Automatic CAD a PDF Converter v7.2.0

## Actualizador más seguro 🍪

- Al aceptar una actualización, la aplicación prepara un proceso auxiliar que **espera a que Python se cierre completamente** antes de ejecutar el instalador.
- El instalador comprueba durante un máximo de 60 segundos si quedan procesos de Automatic CAD a PDF Converter en la misma carpeta y **no sobrescribe archivos mientras estén en uso**.
- Conserva la ubicación de instalación anterior, incluso si el usuario eligió una carpeta personalizada.
- Se mantiene el consentimiento explícito antes de descargar e instalar, así como la verificación SHA-256 del instalador.
- Si hay una conversión en curso, pospone la instalación en lugar de interrumpirla.
- Se conservan visor clásico, mapa con miniaturas, pantalla completa, selección por grupos, papeles A0–A4, PDF único o separado, motor AutoCAD y opción para no abrir PDFs durante la impresión.

## Instalador

**Archivo adjunto que debe publicarse:**
`Setup_Automatic_CAD_a_PDF_Converter_v7_2_0.exe`

**Etiqueta de GitHub:** `v7.2.0` · **Versión estable:** sí · **Prerelease:** no

**SHA-256 del archivo compilado:**
`378759481f317f865d231f7fad29e58b19fc24334de920b1962416a918639c08`

## Verificaciones realizadas

- 47 pruebas automatizadas exitosas, incluyendo las 83 láminas del DXF de Peñón.
- Exportación simulada en PDF conjunto y por separado.
- Comprobación de miniaturas, visor, mapa, selección y formatos.
- Simulación de que la versión 7.1.0 reconoce una versión 7.2.0, descarga el instalador completo y valida SHA-256.
- Simulación del cierre de la aplicación y transferencia de control al ayudante de actualización.
- Ejecutable del instalador y del ayudante compilados en formato PE de Windows de 64 bits.

**Pendiente de probar en un equipo Windows real:** ejecución del asistente de instalación, cierre definitivo de los procesos antes de reemplazar archivos y conversión en AutoCAD 2026. No publicar como versión final validada hasta completar esta prueba.

## Prueba recomendada

1. Mantén instalada la versión 7.1.0.
2. Publica esta versión en GitHub Releases como `v7.2.0`, adjuntando el archivo exacto mencionado.
3. Abre la v7.1.0 y elige descargar la actualización.
4. Confirma que la aplicación se cierra antes de que comience la instalación.
5. Al finalizar, abre el programa y verifica que se muestre **7.2.0**.
6. Comprueba con un DXF pequeño que las funciones del programa sigan funcionando.
