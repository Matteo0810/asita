from pyserv import Application

app = Application()

def listen_callback(error):
    if error:
        raise error
    print(f"Server listening on port 1000.")

app.listen(1000, lambda error: listen_callback(error))