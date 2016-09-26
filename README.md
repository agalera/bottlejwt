# bottlejwt
JWT plugin for bottle

## installation

Via pip:
```pip install bottlejwt```

Or clone:
```git clone https://github.com/kianxineki/bottlejwt.git```


## example server:
```python
from bottle import get, install, run
from bottlejwt import JwtPlugin

def validation(auth, auth_value):
    print(auth, auth_value)
    return True

@get("/", auth="any values and types")
def example(auth):  # auth argument is optional!
    return "ok"


install(JwtPlugin(validation, 'secret', algorithm='HS256'))
run(host="0.0.0.0", port="9988")
```

## Test:
```bash
curl http://localhost:9988/?access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ
```

## Create Token:
```python
from bottlejwt import JwtPlugin

# is a singleton, you only need to initialize once.
# * If you did install () also work
JwtPlugin(validation, 'secret', algorithm='HS256')

print(JwtPlugin.encode({'name': 'pepito'}))
```
