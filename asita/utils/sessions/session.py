class Session:

    def __init__(self, sessionId):
        self.session = {}
        self.sessionId = sessionId

    def get_session_id(self):
        return self.sessionId

    def set(self, key, value):
        self.session[key] = value
    
    def get(self, key):
        if self.has(key):
            return self.session[key]
        return None

    def has(self, key):
        return key in self.session

    def all(self):
        return self.session.items()

    def delete(self, key):
        del self.session[key]

    def __str__(self):
        return "sessionId=" + self.sessionId + ";Path=\"/\";Max-Age=2592000"