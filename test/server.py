from bottle import get, install, app
from bottlejwt import JwtPlugin


def validation(auth, auth_value):
    return auth.get('auth') == auth_value


install(JwtPlugin(validation, 'secret', algorithm='HS256'))


@get("/authenticate", auth=1)
def yes_auth(auth):
    return "ok"


@get("/authenticate_without_argument", auth=1)
def yes_auth_no_argument():
    return "ok"


@get("/without_authenticate")
def no_auth():
    return "ok"


if __name__ == '__main__':
    # run()
    app[0].run(host="0.0.0.0", port="1234")  # pragma: no cover
