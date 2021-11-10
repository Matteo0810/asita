from asita.utils.http_types import HttpMethods

class Route():

    def __init__(self, path: str, request_type: HttpMethods, callback):
        self.path = path
        self.request_type = request_type
        self.callback = callback
    
    def get_method(self) -> str:
        return self.request_type

    def get_path(self) -> str:
        return self.path

    def get_callback(self):
        return self.callback

    def handle(self, request: object, response: object):
        self.callback(request, response)

    def has_method(self, method) -> bool:
        if not isinstance(method, HttpMethods):
            raise Exception("Please make sur your method is an instance of HttpMethods.")
        return method == self.get_method()