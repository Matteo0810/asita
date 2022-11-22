from asita.application import Application

app = Application()

def test(req, res):
    res.send(f"Page requested with HTTP Method '{req.request_type}'")

# post method
app.post("/", lambda req, res: test(req, res))

# get method
app.get("/", lambda req, res: test(req, res))

# put method
app.put("/", lambda req, res: test(req, res))

# delete method
app.delete("/", lambda req, res: test(req, res))

# head method
app.head("/", lambda req, res: test(req, res))

# patch method
app.patch("/", lambda req, res: test(req, res))

# all methods
app.all("/all_methods", lambda req, res: test(req, res))

def listen_callback(error):
    if error:
        raise error
    print("Application listening on port 1000")

app.listen(1000, lambda error: listen_callback(error))
