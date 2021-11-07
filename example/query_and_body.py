from debug import debug
from lib.Application import Application

app = Application()

def get_form(request, response):
    body = request.body
    query = request.query

    debug(f'Query content {query}', True)
    debug(f'Body content {body}', True)

    response.json(body)

app.post("/", lambda req, res: get_form(req, res))

def listen_callback(error):
    if error:
        return debug("Impossible connection", False)
    debug("Application listening on port 1000", True)

app.listen(1000, lambda error: listen_callback(error))