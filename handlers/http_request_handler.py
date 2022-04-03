from http.server import BaseHTTPRequestHandler
import urllib.parse
import traceback

from helpers.dotenv import get_env
from ..utils.http_types import HttpMethods, HttpResponses

from .request import Request
from .response import Response


class HttpRequestHandler(BaseHTTPRequestHandler):

    def __init__(self, routes, asset_directory, *args):

        self.routes = routes
        self.asset_directory = asset_directory
        BaseHTTPRequestHandler.__init__(self, *args)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', get_env('CORS'))
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header('Access-Control-Allow-Headers', '*')
        return super(HttpRequestHandler, self).end_headers()

    def do_GET(self):
        result = self._is_asset()
        response = Response(self)

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

    def do_OPTIONS(self):
        self._handle_route(HttpMethods.OPTIONS)

    def _handle_route(self, method, response=None):
        response = response or Response(self)
        path = self.path.split('?')[0]

        try:
            for route in self.routes:
                if route['path'] == path:
                    route = route['route']
                    if route and (route.has_method(method) or route.has_method(HttpMethods.ALL)):
                        return route.handle(Request(self), response)
            return response.status(HttpResponses.NOT_FOUND) \
                .send(f'Cannot {method.value} {path}')
        except Exception:
            response.send(traceback.format_exc())

    def _is_asset(self):
        if self.asset_directory:
            if self.asset_directory['name'] in self.path:
                path = self.path.replace(self.asset_directory['name'], '')
                path = path.replace('\\', '/')
                path = urllib.parse.unquote(self.asset_directory['directory'] + path)
                file_type = path.split('.').pop()

                if file_type in get_env("ACCEPTED_FILES"):
                    return bytearray(open(path, 'rb').read()), f'image/{file_type}{("", "+xml")[file_type=="svg"]}', False
                elif file_type in get_env("ACCEPTED_FONTS"):
                    return bytearray(open(path, 'rb').read()), f'font/{file_type}', False
                return open(path, 'rb').read(), f"text/{file_type};charset=UTF-8", False
            return False
        return False
