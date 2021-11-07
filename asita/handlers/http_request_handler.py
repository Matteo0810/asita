from http.server import BaseHTTPRequestHandler
from lib.utils.sessions.sessions import Sessions

import traceback

from .request import Request
from lib.utils.http_types import HttpMethods, HttpResponses
from .response import Response

sessions = Sessions()

class HttpRequestHandler(BaseHTTPRequestHandler):

    def __init__(self, routes, asset_directory, *args):
        global sessions

        self.routes = routes
        self.sessions = sessions
        self.asset_directory = asset_directory
        BaseHTTPRequestHandler.__init__(self, *args)

    def do_GET(self):
        result = self._is_asset()
        response = Response(self, self.sessions)

        if result:
            data, type, encoded = result
            return response.send(data, type, encoded)
        return self._handle_route(HttpMethods.GET, response)

    def do_POST(self):
        self._handle_route(HttpMethods.POST)

    def do_HEAD(self):
        self._handle_route(HttpMethods.HEAD)

    def do_PATCH(self):
        self._handle_route(HttpMethods.PATCH)

    def do_PUT(self):
        self._handle_route(HttpMethods.PUT)

    def do_DELETE(self):
        self._handle_route(HttpMethods.DELETE)
    
    def _handle_route(self, method, response = None):
        response = response or Response(self, self.sessions)
        path = self.path.split('?')[0]

        try: 
            for route in self.routes:
                if route['path'] == path:
                    route = route['route']
                    if route and (route.has_method(method) or route.has_method(HttpMethods.ALL)):
                        return route.handle(Request(self, self.sessions), response)
            return response.status(HttpResponses.NOT_FOUND) \
                .send(f'Cannot {method.value} {path}')
        except Exception:
            response.send(traceback.format_exc())

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