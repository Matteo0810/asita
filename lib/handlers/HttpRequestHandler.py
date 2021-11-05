from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler

from .Request import Request
from lib.utils.HttpTypes import HttpMethods
from .Response import Response

cookies = SimpleCookie()

class HttpRequestHandler(BaseHTTPRequestHandler):

    def __init__(self, routes, asset_directory, *args):
        global cookies

        self.routes = routes
        self.cookie = cookies
        self.asset_directory = asset_directory
        BaseHTTPRequestHandler.__init__(self, *args)

    def do_GET(self):
        result = self._is_asset()
        response = Response(self, self.cookie)

        if result:
            data, type, encoded = result
            return response.send(data, type, encoded, True)
        return self._handle_route(response, HttpMethods.GET)

    def do_POST(self):
        self._handle_route(Response(self, self.cookie), HttpMethods.POST)

    def do_HEAD(self):
        self._handle_route(Response(self, self.cookie), HttpMethods.HEAD)

    def do_PATCH(self):
        self._handle_route(Response(self, self.cookie), HttpMethods.PATCH)

    def do_PUT(self):
        self._handle_route(Response(self, self.cookie), HttpMethods.PUT)

    def do_DELETE(self):
        self._handle_route(Response(self, self.cookie), HttpMethods.DELETE)
    
    def _handle_route(self, response, method):
        path = "/" + self.path.split('?')[0]
        if path not in self.routes:
            return response.send(f'Cannot {method.value} {self.path}')
        try: 
            route = self.routes[path]
            if route and (route.has_method(method) or route.has_method(HttpMethods.ALL)):
                return route.handle(Request(self), response)
            return response.send(f'Cannot {method.value} {self.path}')
        except Exception as error:
            response.send(str(error.with_traceback()))

    def _is_asset(self):
        if self.asset_directory:
            if self.asset_directory['name'] in self.path:
                path = self.path.replace(self.asset_directory['name'], '')
                path = path.replace('\\', '/')
                path = self.asset_directory['directory'] + path
                type = path.split('.').pop()
                
                if type in ['png', 'jpg', 'gif', 'jfif', 'wepb', 'svg']:
                    return (bytearray(open(path, 'rb').read()), f'image/{type}', False)
                return (open(path, 'r').read(), f"text/{type}", True)
            return False
        return False