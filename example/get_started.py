from asita.application import Application

app = Application()

def listen_callback(error):
    if error:
        raise error
    print("Application listening on port 1000")

app.listen(1000, lambda error: listen_callback(error))