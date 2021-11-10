import uuid

from .session import Session

class Sessions:

    def __init__(self):
        self.sessions = dict()

    def add(self) -> Session:
        sessionId = uuid.uuid1().hex
        session = Session(sessionId)
        self.sessions[sessionId] = session
        return session

    def all(self) -> object:
        return self.sessions.items()

    def has(self, sessionId: str) -> bool:
        return sessionId in self.sessions

    def get(self, sessionId: str) -> Session:
        if self.has(sessionId):
            return self.sessions[sessionId]
        return Session(Sessions.random_session_id())

    def delete(self, sessionId: str):
        del self.sessions[sessionId]
        return self

    @staticmethod
    def random_session_id() -> str:
        return uuid.uuid1().hex