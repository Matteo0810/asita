from http.server import HTTPServer
import json

from .utils.HttpTypes import HttpMethods
from .handlers.HttpRequestHandler import HttpRequestHandler
from .utils.Route import Route

class Application():

    def __init__(self):
        self.instance = None
        self.routes = {}
        self.asset_directory = {}
        pass

    def all(self, path, callback):
        self._add_route(path, HttpMethods.ALL, callback)

    def post(self, path, callback):
        self._add_route(path, HttpMethods.POST, callback)

    def get(self, path , callback):
        self._add_route(path, HttpMethods.GET, callback)

    def put(self, path, callback):
        self._add_route(path, HttpMethods.PUT, callback)

    def patch(self, path, callback):
        self._add_route(path, HttpMethods.PATCH, callback)
        
    def delete(self, path, callback):
        self._add_route(path, HttpMethods.DELETE, callback)

    def head(self, path, callback):
        self._add_route(path, HttpMethods.HEAD, callback)

    def define_asset(self, name, directory):
        self.asset_directory = {
            "name": name,
            "directory": directory
        }

    def listen(self, port, callback):
        if not callback or not hasattr(callback, '__call__'):
            raise ValueError("Callback doit être une fonction.")
        if not port and type(port) is not int:
            callback(ValueError("Aucun port précisé."))
        try:
            callback(None)
            self.instance = HTTPServer(('localhost', port), self._get_handler)
            self.instance.serve_forever()
        except:
            callback(ConnectionError("Impossible de se connecter"))

    def _add_route(self, path, request_type, callback):
        if not path or type(path) is not str:
            raise ValueError("Chemin invalide.")
        if not callback or not hasattr(callback, '__call__'):
            raise ValueError("Callback doit être une fonction.")

        path = "/" + path
        self.routes[path] = Route(path, request_type, callback)

    def _get_handler(self, *args):
        HttpRequestHandler(self.routes, self.asset_directory, *args)