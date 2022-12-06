[![pythonversions](https://img.shields.io/pypi/pyversions/bottlejwt.svg)](https://pypi.python.org/pypi/bottlejwt)
[![Codecov](https://img.shields.io/codecov/c/github/agalera/bottlejwt.svg)](https://codecov.io/github/agalera/bottlejwt)
[![Travis](https://img.shields.io/travis/agalera/bottlejwt.svg)](https://travis-ci.org/agalera/bottlejwt)

# bottlejwt
JWT plugin for bottle

## installation

Via pip:
```pip install bottlejwt```

Or clone:
```git clone https://github.com/agalera/bottlejwt.git```


## example server:
```python
import time

from bottlejwt import JwtPlugin
from bottle import Bottle, request


permissions = {"user": 0, "service": 1, "admin": 2}
jwt_secret_key = "s3cr3tk3y!!ch@ng3m3"

def validation(auth, auth_value):
    return permissions[auth["type"]] >= permissions[auth_value]

app = Bottle()
app.install(JwtPlugin(validation, jwt_secret_key, algorithm="HS512"))

@app.post("/login")
def login():
    """
    receive:
    {'client_id': 'user',
     'client_secret': 'password'
    }

    response:
    {'access_token': 'token',
     'type': 'bearer'}

    """
    # example for mongodb
    '''
    user = db.users.find_one(
        {
            "client_id": request.json["client_id"],
            "client_secret": hash_password(request.json["client_secret"]),
        },
        {"_id": False, "client_secret": False},
    )
    '''
    # Any data we consider good, implement a logic instead of doing this
    user = {
        "client_id": request.json["client_id"],
        "type": "user"
    }
    if not user:
        raise HTTPError(403, "Invalid user or password")
    user["exp"] = time.time() + 86400  # 1 day
    return {"access_token": JwtPlugin.encode(user), "type": "bearer"}

@app.get('/jwt_info', auth='user')
def jwt_info(auth):
    return auth

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9999)
```

## Test by curl:
```bash
curl http://localhost:9988/?access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ
```
## Example client:
```python
import requests

response = requests.post(
    'http://localhost:9999/login',
    json={
        'client_id': 'user',
        'client_secret': 'password'
    }
).json()

token = f"{response['type']} {response['access_token']}"

# option 1 - Headers
requests.get(
    'http://localhost:9999/jwt_info',
    headers={'Authorization': token}
)
# response
'''
{'client_id': 'user',
 'type': 'user',
 'exp': 1670421559.047136,
 'token': '...'
}
'''

# option 2 - url argument
requests.get(
    f'http://localhost:9999/jwt_info?access_token={response["access_token"]}',
)

'''
{'client_id': 'user',
 'type': 'user',
 'exp': 1670421559.047136,
 'token': '...'
}
'''
```
## Create Token:
```python
from bottlejwt import JwtPlugin

# is a singleton, you only need to initialize once.
# * If you did install () also work
JwtPlugin(validation, 'secret', algorithm='HS256')

print(JwtPlugin.encode({'name': 'pepito'}))
```
