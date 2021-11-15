from asita.application import Application

app = Application()

def get_form(request, response):
    response.json({
        "body": request.body,
        "query": request.query,
        "params": request.params
    })

app.post("/", lambda req, res: get_form(req, res))

def listen_callback(error):
    if error:
        raise error
    print("Application listening on port 1000")

app.listen(1000, lambda error: listen_callback(error))
