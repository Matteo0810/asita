from lib.utils.http_types import HttpMethods

class Route():

    def __init__(self, path, request_type, callback):
        self.path = path
        self.request_type = request_type
        self.callback = callback
    
    def get_method(self):
        return self.request_type

    def get_path(self):
        return self.path

    def handle(self, request, response):
        self.callback(request, response)

    def has_method(self, method):
        if not isinstance(method, HttpMethods):
            raise Exception("Please make sur your method is an instance of HttpMethods.")
        return method == self.get_method()