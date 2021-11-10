class Session:

    def __init__(self, sessionId: str):
        self.session = {}
        self.sessionId = sessionId

    def get_session_id(self):
        return self.sessionId

    def set(self, key: str, value: str):
        self.session[key] = value
    
    def get(self, key: str):
        if self.has(key):
            return self.session[key]
        return None

    def has(self, key: str):
        return key in self.session

    def all(self) -> object:
        return self.session.items()

    def delete(self, key: str):
        del self.session[key]

    def __str__(self) -> str:
        return "sessionId=" + self.sessionId + ";Path=\"/\";Max-Age=2592000"