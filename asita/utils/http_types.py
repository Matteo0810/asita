from enum import Enum

class HttpResponses(Enum):
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    BAD_REQUEST = 400

    OK = 200
    NO_CONTENT = 204

    INTERNAL_SERVER_ERROR = 500

class HttpMethods(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    HEAD = "HEAD"
    PATCH = "PATCH"
    ALL = "ALL"
    OPTIONS = "OPTIONS"