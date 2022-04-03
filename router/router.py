from .route import Route
from ..utils.http_types import HttpMethods


class Router:

    def __init__(self, default_path: str = ""):
        self.default_path = default_path
        self.routes = list()

    def set_default_path(self, default_path: str):
        self.default_path = default_path

    def use(self, path: str, router):
        if not isinstance(router, Router):
            raise Exception("router must be Router object.")
        router.set_default_path(path)
        for data in router.get_routes():
            route = data['route']
            self._add_route(f'{router.default_path}{route.get_path()}', route.get_method(), route.get_callback())

    def all(self, path: str, callback):
        self._add_route(path, HttpMethods.ALL, callback)

    def post(self, path: str, callback):
        self._add_route(path, HttpMethods.POST, callback)

    def get(self, path: str, callback):
        self._add_route(path, HttpMethods.GET, callback)

    def put(self, path: str, callback):
        self._add_route(path, HttpMethods.PUT, callback)

    def patch(self, path: str, callback):
        self._add_route(path, HttpMethods.PATCH, callback)

    def delete(self, path: str, callback):
        self._add_route(path, HttpMethods.DELETE, callback)

    def head(self, path: str, callback):
        self._add_route(path, HttpMethods.HEAD, callback)

    def _add_route(self, path: str, request_type: HttpMethods, callback):
        self.routes.append({
            "path": self.default_path + path,
            "route": Route(path, request_type, callback)
        })

    def get_routes(self) -> list:
        return self.routes
