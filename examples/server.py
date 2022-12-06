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