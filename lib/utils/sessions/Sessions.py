import uuid
from .Session import Session

class Sessions:

    def __init__(self):
        self.sessions = dict()

    def add(self):
        sessionId = uuid.uuid1().hex
        session = Session(sessionId)
        self.sessions[sessionId] = session
        return session

    def all(self):
        return self.sessions.items()

    def has(self, sessionId):
        return sessionId in self.sessions

    def get(self, sessionId):
        if self.has(sessionId):
            return self.sessions[sessionId]
        return Session(Sessions.random_session_id())

    def delete(self, sessionId):
        del self.sessions[sessionId]
        return self

    @staticmethod
    def random_session_id():
        return uuid.uuid1().hex