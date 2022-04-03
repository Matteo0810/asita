import json
from os.path import exists

from ..utils.http_types import HttpResponses


class Response:

    def __init__(self, data):
        self.data = data
        self.headers = {}
        self.currentStatus = HttpResponses.OK
        self.statusHandled = False

    def status(self, code: int):
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

    def set_header(self, key: str, value: str):
        self.headers[key] = value
        return self

    def send_header(self, key: str, value: str):
        self.data.send_header(key, value)
        return self

    def send(self, data: object, content_type: str = None, encoded: bool = True):
        if isinstance(data, dict):
            raise TypeError('invalid type, use json() instead.')
        self.status(self.currentStatus) \
            .set_header("Content-type", (content_type, "text/plain")[not content_type])
        if self.headers:
            for key, value in self.headers.items():
                self.send_header(key, value)
        self.data.end_headers()
        self.data.wfile.write(data.encode("utf_8") if encoded else data)
        return self

    def json(self, data: dict):
        return self.send(json.dumps(data), "application/json")

    def render(self, path: str):
        if not path.startswith('./'):
            path = "./" + path
        if not path.endswith(".html"):
            path += ".html"
        if not exists(path):
            raise FileNotFoundError("HTML file not found.")
        return self.send(bytes(open(path, 'r').read(), 'utf-8'), "text/html", False)
