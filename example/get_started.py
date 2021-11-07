from debug import debug
from lib.Application import Application

app = Application()

def listen_callback(error):
    if error:
        return debug("Impossible connection", False)
    debug("Application listening on port 1000", True)

app.listen(1000, lambda error: listen_callback(error))