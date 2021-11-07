import json

from debug import debug
from lib.Application import Application

app = Application()

# you can also get the current session

def get_session(request, response):
    debug(f'Session: {request.session}', True)
    response.send(f'Session: {request.session}')

# add object to the session

def add_session(request, response):
    session = request.session
    session.set("user_data", json.dumps({
        "name": "Mario",
        "age": 40
    }))
    debug('Session changed !', True)
    response.send('Session changed !')

app.get("/", lambda req, res: get_session(req, res))

app.post("/add_session", lambda req, res: add_session(req, res))

def listen_callback(error):
    if error:
        return debug("Impossible connection", False)
    debug("Application listening on port 1000", True)

app.listen(1000, lambda error: listen_callback(error))