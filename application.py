from http.server import HTTPServer

from .handlers.http_request_handler import HttpRequestHandler

from .router.router import Router

class Application(Router):

    def __init__(self):
        super().__init__()

        self.instance = None
        self.asset_directory = {}
        pass

    def define_asset(self, name: str, directory: str):
        self.asset_directory = {
            "name": name,
            "directory": directory
        }

    def listen(self, port: int, callback):
        if not port and type(port) is not int:
            callback(ValueError("No port found."))
        try:
            callback(None)
            self.instance = HTTPServer(('localhost', port), self._get_handler)
            self.instance.serve_forever()
        except:
            callback(ConnectionError("Impossible connection"))

    def _get_handler(self, *args):
        HttpRequestHandler(self.get_routes(), self.asset_directory, *args)