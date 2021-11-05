import base64

class CookieParser:

    def __init__(self, cookie):
        self.cookie = cookie
    
    def add(self, key, value):
        self.cookie[key] = str(base64.b64encode(value.encode('utf-8')), 'utf-8')
        return self

    def get(self, key):
        return self.cookie[key]

    def delete(self, key):
        del self.cookie[key]
        return self

    def __str__(self):
        cookie = self.cookie.output(header='', sep='')
        cookie = cookie + ";Path=\"/\";Max-Age=2592000"
        return cookie

    @staticmethod
    def parse(cookie):
        return CookieParser(cookie)