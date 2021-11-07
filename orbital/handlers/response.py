import json
from os.path import exists

from lib.utils.http_types import HttpResponses 

class Response():

    def __init__(self, data, sessions):
        self.data = data
        self.headers = {}
        self.sessions = sessions
        self.currentStatus = HttpResponses.OK
        self.statusHandled = False
        

    def status(self, code):
        if not isinstance(code, HttpResponses):
            raise Exception("Please, make sur this is an instance of HTTPResponses")
        self.currentStatus = code
        if not self.statusHandled:
            self.statusHandled = True
            self.data.send_response_only(self.currentStatus.value)
        return self

    def end(self):
        self.data.flush_headers()
        return self

    def set_header(self, key, value):
        self.headers[key] = value
        return self

    def send_header(self, key, value):
        self.data.send_header(key, value)
        return self
        
    def send(self, data, type = None, encoded = True):
        self.status(self.currentStatus) \
            .set_header("Content-type", (type, "text/plain")[not type])
        self._store_session()
        if self.headers:
            for key, value in self.headers.items():
                self.send_header(key, value)
        self.data.end_headers()
        self.data.wfile.write(data.encode("utf_8") if encoded else data)
        return self

    def _store_session(self):
        cookie = self.data.headers.get('Cookie')

        if (not cookie) or (cookie and not self.sessions.has(cookie.split('=').pop())):
            session = self.sessions.add()
            self.set_header("Set-Cookie", session)
    
    def json(self, data):
        return self.send(json.dumps(data), "application/json")

    def render(self, path):
        if not path.startswith('./'):
            path = "./" + path
        if not path.endswith(".html"):
            path += ".html"
        if not exists(path):
            raise FileNotFoundError("HTML file not found.")
        file = open(path, 'r', encoding="utf-8")
        return self.send(file.read().replace('\n', ''), "text/html")