import json
from os.path import exists

from lib.utils.HttpTypes import HttpResponses
from lib.utils.CookieParser import CookieParser 

class Response():

    def __init__(self, data, cookie):
        self.data = data
        self.cookie = CookieParser.parse(cookie)

    def status(self, code):
        if not isinstance(code, HttpResponses):
            raise Exception("Please, make sur this is an instance of HTTPResponses")
        self.data.send_response_only(code.value)
        return self

    def end(self):
        self.data.flush_headers()
        return self

    def set_header(self, key, value):
        self.data.send_header(key, value)
        return self

    def update_cookie(self, cookie):
        self.cookie = cookie
        return self
        
    def send(self, data, type = None, encoded = True, is_asset = False):
        self.status(HttpResponses.OK) \
            .set_header("Content-type", (type, "text/plain")[not type])
        if self.cookie or not is_asset:
            self.set_header("Set-Cookie", self.cookie)
        self.data.end_headers()
        self.data.wfile.write(data.encode("utf_8") if encoded else data)
        return self
    
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