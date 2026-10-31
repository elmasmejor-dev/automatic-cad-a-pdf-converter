# 🍪 Automatic CAD a PDF Converter v7.2.11

## Actualización estable para DXF

Esta versión mantiene todas las funcionalidades de la v7.2.10 e introduce una recuperación más robusta frente a errores de comunicación con AutoCAD al imprimir hojas mediante `PlotToFile`.

### Mejoras

- **Recuperación de `PlotToFile` en todas las páginas:** ante ciertos errores COM, comprueba si se creó el PDF antes de reintentar.
- **Reconfiguración del trazado:** cuando es posible, reactiva el dibujo, prepara el trazador y vuelve a intentar la impresión de la hoja afectada.
- **Diagnóstico detallado:** registra detalles del fallo y códigos HRESULT para investigar problemas persistentes.
- **Protección contra duplicados:** no incorpora dos veces la misma página al recuperarse de un fallo.
- **Seguridad de exportación:** si una página no puede exportarse tras la recuperación, se detiene sin sustituir el PDF anterior ni entregar un documento final parcial.
- Conserva **Vaciar lista**, eliminación individual de láminas, sobrescritura segura y todas las mejoras estables anteriores.
- Incluye Python 3.12 y dependencias: **no necesitas instalar Python por separado**.

### Requisitos

- Windows 10 u 11 de 64 bits.
- AutoCAD instalado para el motor de impresión de máxima fidelidad.
- La importación **DWG directa sigue en versión beta separada**. Esta edición estable utiliza DXF.

### Verificación

- Compilación de prueba en Windows superada y artefacto previo comprobado por SHA-256.
- Pruebas automáticas de recuperación y de fallos simulados, incluyendo diferentes posiciones y varios errores en una misma exportación.
- **Estas pruebas no garantizan la recuperación de todos los errores reales de AutoCAD.** Si el problema está en el trazador, el dibujo o una hoja concreta, puede requerir diagnóstico adicional.

### Actualización

El instalador oficial `Setup_Automatic_CAD_a_PDF_Converter_v7_2_11.exe` conserva la identidad, ruta y accesos directos de las versiones estables anteriores, por lo que actualiza la instalación existente.

**Creado por Manu · Hecho con GPT**
