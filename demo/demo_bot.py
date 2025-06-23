import json
import os

class DemoAutoPoster:
    """Versión de demostración que simula publicaciones."""

    def __init__(self, token, group_id, json_file):
        self.token = token
        self.group_id = group_id
        self.json_file = json_file

    def fetch_content(self):
        try:
            with open(self.json_file, 'r', encoding='utf-8') as fh:
                return json.load(fh)
        except Exception as exc:
            print(f"No se pudo leer el contenido: {exc}")
            return None

    def post_to_group(self, message, link=None):
        print(f"[DEMO] Publicando en {self.group_id} con token {self.token[:4]}...")
        print(f"Mensaje: {message}")
        if link:
            print(f"Link: {link}")
        print("\n")

    def autopost(self):
        content = self.fetch_content()
        if not content:
            print("No hay contenido para publicar")
            return
        self.post_to_group(content.get('message'), content.get('link'))


if __name__ == '__main__':
    token = os.getenv('TOKEN', 'demo-token')
    group_id = os.getenv('GROUP_ID', '000000')
    json_file = os.getenv('JSON_FILE', 'post.json')

    demo = DemoAutoPoster(token, group_id, json_file)
    demo.autopost()
