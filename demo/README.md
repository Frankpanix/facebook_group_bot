# Versión de demostración

Esta carpeta contiene un ejemplo simplificado del bot que **no** realiza
peticiones reales al API de Facebook. Su objetivo es mostrar de forma
básica cómo funcionaría el proceso de publicación.

## Uso

1. Asegúrate de tener Python 3 instalado.
2. Desde esta carpeta ejecuta:
   ```bash
   python demo_bot.py
   ```
   También puedes definir las variables de entorno `TOKEN`, `GROUP_ID` y
   `JSON_FILE` para personalizar la ejecución.

El script leerá el archivo `post.json` y mostrará por consola una
simulación de la publicación.
