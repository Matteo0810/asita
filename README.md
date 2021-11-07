# What is Asita ?
**Asita** is a **web application framework for python**. It is designed to be easy to use and be more easy for **javascript users** to use python frameworks because it is based on **express-js framework**.

![License](https://img.shields.io/github/license/Matteo0810/PyServ.svg)

## How to install Asita ?

Install this package using [pip](https://pip.pypa.io/en/stable/getting-started/)

`$ pip install asita`

# Documentation

## Get started

### Exemple

```python
from asita import Application

# creating application instance
app = Application()

# callback when web server is ready
def listen_callback(error):
    if error:
        raise error
    print(f"Server listening on port 1000.")

# listen the webserver on port (for instance port 1000)
app.listen(1000, lambda error: listen_callback(error))
```

### **Application** class

#### Methods

| Name | Parameters | Description | 
|------|:-----------:|:----------:|
| all(**path**, **callback**) | path: **string**, callback: **function** | Routes an HTTP request, where **all** is the HTTP method such as GET, PUT, POST, OATCH, DELETE, HEAD |
| post(**path**, **callback**) | path: **string**, callback: **function** | Routes HTTP POST requests |
| get(**path**, **callback**) | path: **string**, callback: **function** | Routes HTTP GET requests |
| put(**path**, **callback**) | path: **string**, callback: **function** | Routes HTTP PUT requests |
| patch(**path**, **callback**) | path: **string**, callback: **function** | Routes HTTP PATCH requests |
| delete(**path**, **callback**) | path: **string**, callback: **function** | Routes HTTP DELETE requests |
| head(**path**, **callback**) | path: **string**, callback: **function** | Routes HTTP HEAD requests |
| define_asset(**name**, **directory**) | name: **string**, directory: **string** | Define the asset directory access |
| listen(**port**, **callback**) | port: **integer**, callback: **function** | start listening a port |

## Create a route

### Exemple

```python
# some awesome things check request and response methods :-)
def home(request, response):
    pass

# "/" is the default path
app.all("/", lambda req, res: home(req, res))
```

> To see more example, check the example file.

### **Request** class

#### Attributs

| Name | Description | 
|------|:-----------:|
| headers | headers of the request |
| session | client session |
| path | the url's path |
| request_type | type of request |
| server_address | address of the requested server |
| server_version | version of the requested server |
| protocol_version | version of the HTTP protocol |
| body | the body content of the POST request |
| query | url params |

#### Methods

| Name | Parameters | Description | 
|------|:-----------:|:----------:|
| get(**value**) | value: **string** | get a header of the request |
| accepts() | none | get types which are accepted |

### **Response** class

#### Methods

| Name | Parameters | Description | 
|------|:-----------:|:----------:|
| status(**code**) | code: **HttpResponses** | return the response's state |
| set_header(**key**, **value**) | key: **string**, value: **string** | add/update headers |
| send(**data**, **type?**, **encoded?**) | data: **object**, type: **string**, encoded: **boolean**, is_asset: **boolean** | send response |
| json(**data**) | data: **dict** | write json on a page |
| render(**path**) | path: **string** | render **html** file. |
| end() | none | stop the current request |

> **?** means that it is optionnal

### **Sessions** class

| Name | Parameters | Description | 
|------|:-----------:|:----------:|
| add() | none | create new empty session |
| all() | none | get all sessions |
| has(**sessionId**) | key: **string** | verify if a session exists |
| get(**sessionId**) | key: **string** | get a session by id |
| delete(**sessionId**) | key: **string** | delete session by id  |
| radnom_session_id **@Static method** | none | get all sessions |

### **Session** class

| Name | Parameters | Description | 
|------|:-----------:|:----------:|
| get_session_id | none | get the id of the session |
| set(**key**, **value**) | key: **string**, value: **string** | add data to the client session |
| has(**key**) | key: **string** | verify if client session has the selected data |
| get(**key**) | key: **string** | get data from client session |
| delete(**key**) | key: **string** | delete data from client session  |
| all() | none | get client session data |

## Enumerations

### **HttpMethods**

| HTTP Methods |
|------|
| GET |
| POST |
| PUT |
| DELETE |
| PATCH |
| HEAD |
| ALL |

### **HttpResponses**

#### Client side

| Response types | Codes |
|------|:------:|
| OK | **200** |
| NO_CONTENT | **204** |
| UNAUTHORIZED | **401** |
| FORBIDDEN | **403** |
| NOT_FOUND | **404** |
| BAD_REQUEST | **400** |

#### Server side

| Response types | Codes |
|------|:------:|
| INTERNAL_SERVER_ERROR | **500** |

# License

__MIT LICENSE__
