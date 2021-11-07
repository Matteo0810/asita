import json
from asita.utils.sessions.session import Session
from asita.utils.sessions.sessions import Sessions

class Request():
    
    def __init__(self, data, sessions):
        """
            Permet de récupérer les informations d'une requête
            data: BaseHTTPRequestHandler, les informations de la requête
        """
        self.data = data
        self.sessions = sessions
        self.headers = data.headers
        self.path = data.path
        self.request_type = data.command
        self.server_address = data.client_address
        self.server_version = data.server_version
        self.protocol_version = data.protocol_version

        self.query = self._parse_query()
        self.body = self._parse_body()
        self.session = self._parse_session()

    def _parse_session(self):
        cookie = self.get('Cookie')
        if cookie:
            return self.sessions.get(cookie.split('=').pop())
        return Session(Sessions.random_session_id())

    def _parse_body(self):
        content_length = self.get('Content-Length')
        result = {}
        
        if content_length:
            body = self.data.rfile.read(int(content_length))
            if body:
                body = body.decode('utf8').replace("'", '"')
                result = json.loads(body)
        return result

    def _parse_query(self):
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
        return self.headers.get(value)

    def accepts(self):
        return self.headers.get("accept")