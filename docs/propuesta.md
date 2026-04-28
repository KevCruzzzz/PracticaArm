# Propuesta del proyecto

## Problema

Muchos estudiantes toman notas dispersas mientras estudian (papelitos, chats, apps distintas) y luego batallan para repasar. Hace falta una herramienta sencilla que se pueda abrir rápido desde la terminal.

## Solución propuesta

Construir un **Asistente de Estudio CLI** en Python estándar, con un menú corto y acciones básicas:

- Capturar notas.
- Capturar preguntas de repaso.
- Registrar recordatorios puntuales.
- Mostrar un resumen de la sesión.

La meta es reducir fricción: abrir, escribir, continuar estudiando.

## Alcance

### En alcance (MVP)

- Aplicación de terminal interactiva.
- Menú principal con opciones numeradas.
- Almacenamiento en memoria por sesión.
- Mensajes y documentación en español (México).

### Fuera de alcance (por ahora)

- Base de datos.
- Interfaz gráfica.
- APIs externas o modelos de pago.
- Sincronización en la nube.

## Criterios de éxito

- El proyecto corre con `python3 src/main.py` sin dependencias extra.
- El usuario puede completar un flujo básico en menos de 2 minutos.
- La documentación permite levantar el proyecto en una lectura rápida.
