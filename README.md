# Asistente de Estudio (CLI)

Proyecto pequeño en Python para ayudarte a estudiar desde la terminal. Está pensado para correr localmente, sin dependencias externas ni servicios de pago.

## ¿Qué hace?

El asistente ofrece un menú simple para:

1. Guardar notas rápidas de estudio.
2. Registrar preguntas para repasar después.
3. Ver recordatorios sugeridos por sesión.
4. Consultar un resumen de lo capturado en la sesión actual.

> Nota: esta versión es **viable y mínima**. Guarda la información en memoria durante la ejecución.

## Requisitos

- Python 3.10+ (funciona con versiones modernas de Python 3).
- Terminal en Linux/macOS (o Git Bash / WSL en Windows).

## Estructura rápida

- `src/main.py`: punto de entrada del asistente.
- `scripts/run.sh`: script de ejecución rápida.
- `docs/`: documentación del proyecto.
- `tests/test_plan.md`: notas de pruebas manuales.

## Cómo ejecutar

### Opción 1: ejecución directa

```bash
python3 src/main.py
```

### Opción 2: script

```bash
chmod +x scripts/run.sh
./scripts/run.sh
```

## Flujo de uso esperado

1. Arranca el programa.
2. Elige una opción del menú (1 a 5).
3. Captura texto cuando se te pida.
4. Repite hasta elegir salir.

## Ejemplo de sesión

```text
=== Asistente de Estudio ===
1) Agregar nota
2) Agregar pregunta
3) Agregar recordatorio
4) Ver resumen
5) Salir
Selecciona una opción: 1
Escribe tu nota: Repasar derivadas parciales.
✅ Nota guardada.
```

## Alcance de esta versión

Incluye:

- CLI funcional con ciclo principal.
- Persistencia en memoria para sesión activa.
- Mensajes claros en español (México).

No incluye todavía:

- Guardado en archivos.
- Fechas automáticas o calendario.
- Integración con servicios externos.

## Próximos pasos sugeridos

- Guardar notas y preguntas en JSON local.
- Agregar etiquetas por materia (ej. mate, historia, inglés).
- Añadir modo “repaso rápido” con preguntas aleatorias.

## Licencia

Uso libre para fines educativos y de práctica.
