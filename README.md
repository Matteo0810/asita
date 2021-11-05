# What is PyServ ?
**PyServ** is a **web application framework for python**. It is designed to be easy to use and be more easy for **express-js users** to use python frameworks because it is based on **express-js framework**.

![Download Count](https://img.shields.io/github/downloads/Matteo0810/PyServ/total) ![License](https://img.shields.io/packagist/l/Matteo0810/PyServ) 

## How to install PyServ ?

installing and update using [pip](https://pip.pypa.io/en/stable/getting-started/)

`$ pip install PyServ`

# Documentation

## Create web application

### Exemple

```python
# import the PyServ web application
from pyserv import Application

# creating application instance
app = Application()

# listen the webserver on port (for instance port 1000)
app.listen(1000, lambda: error: listen_callback(error))

# callback when web server is ready
def listen_callback(error):
    if error:
        raise error
    print(f"Server listening on port 1000.")
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
# import the PyServ web application
from pyserv import Application

# creating application instance
app = Application()

# "/" is the default path
app.all("/", home)

# some awesome things check request and response methods :-)
def home(request, response):
    pass

# check the first step :-)
....
```

### **Request** class

#### Attributs

| Name | Description | 
|------|:-----------:|
| headers | headers of the request |
| session | session of user, stored in cookie |
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
| send(**data**, **type?**, **encoded?**, **is_asset?**) | data: **object**, type: **string**, encoded: **boolean**, is_asset: **boolean** | send response |
| json(**data**) | data: **dict** | write json on a page |
| render(**path**) | path: **string** | render **html** file. |
| end() | none | stop the current request |

> **?** means that it is optionnal

### **HttpMethods** class (Enumeration)

| HTTP Methods |
|------|
| GET |
| POST |
| PUT |
| DELETE |
| PATCH |
| HEAD |
| ALL |

### **HttpResponses** class (Enumeration)

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
