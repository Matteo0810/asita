import json, base64

class Request():
    
    def __init__(self, data):
        """
            Permet de récupérer les informations d'une requête
            data: BaseHTTPRequestHandler, les informations de la requête
        """
        self.data = data
        self.headers = data.headers
        self.session = self._parse_session()
        self.path = data.path
        self.request_type = data.command
        self.server_address = data.client_address
        self.server_version = data.server_version
        self.protocol_version = data.protocol_version

        self.query = self._parse_query()
        self.body = self._parse_body()
    
    def _parse_session(self):
        """
            permet de récupérer la session
        """
        try:
            value = self.get('Cookie')
            value = value.split('session=').pop()
            value = base64.b64decode(value)
            value = str(value, 'utf-8')
            return json.loads(value)
        except:
            return {}

    def _parse_body(self):
        """
            permet de récupérer le contenu du body
            envoyé par l'utilisateur lors d'une requête POST.
        """
        content_length = self.get('Content-Length')
        result = {}
        
        if content_length:
            body = self.data.rfile.read(int(content_length))
            if body:
                body = body.decode('utf8').replace("'", '"')
                result = json.loads(body)
        return result

    def _parse_query(self):
        """
            récupérer la query dans la requête
            retourne un dictionnaire
        """
        chars = self.path.split('?')
        if len(chars) < 2:
            return {}
        chars = chars.pop().split('&')
        queries = {}
        for char in chars:
            char = char.split('=')
            queries[char[0]] = char[1]
        return queries

    def get(self, value):
        """
            récupérer une entête spécifique
            value: str, l'entête voulant être récupéré
            retourne un str, l'entête voulu
        """
        return self.headers.get(value)

    def accepts(self):
        """
            savoir les type de valeur acceptés par l'entête
        """
        return self.headers.get("accept")