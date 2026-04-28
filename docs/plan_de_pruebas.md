# Plan de pruebas

## Objetivo

Validar que el Asistente de Estudio funcione de manera confiable en su versión mínima CLI.

## Alcance de pruebas

- Menú principal y navegación.
- Captura de nota, pregunta y recordatorio.
- Visualización de resumen.
- Manejo de opción inválida.
- Salida del programa.

## Estrategia

Se aplicarán pruebas manuales guiadas, dado que el MVP es pequeño y de interacción por terminal.

## Casos de prueba

### CP-01: Arranque exitoso

- **Precondición:** Python 3 disponible.
- **Paso:** ejecutar `python3 src/main.py`.
- **Resultado esperado:** aparece el menú principal.

### CP-02: Alta de nota

- **Paso:** elegir opción 1 y escribir una nota.
- **Resultado esperado:** mensaje de confirmación y nota visible en resumen.

### CP-03: Alta de pregunta

- **Paso:** elegir opción 2 y escribir una pregunta.
- **Resultado esperado:** confirmación y pregunta visible en resumen.

### CP-04: Alta de recordatorio

- **Paso:** elegir opción 3 y escribir recordatorio.
- **Resultado esperado:** confirmación y recordatorio visible en resumen.

### CP-05: Opción inválida

- **Paso:** escribir `9` u otro valor no permitido.
- **Resultado esperado:** mensaje de advertencia sin cerrar programa.

### CP-06: Salida

- **Paso:** elegir opción 5.
- **Resultado esperado:** mensaje de despedida y cierre sin error.

## Criterio de aceptación

El MVP se considera válido si todos los casos CP-01 a CP-06 se cumplen en una ejecución manual.
