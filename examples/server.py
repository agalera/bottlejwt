from bottle import get, install, run
from bottlejwt import JwtPlugin

def validation(auth, auth_value):
    print(auth, auth_value)
    return True

@get("/", auth="any values and types")
def example(auth):  # auth argument is optional!
    return "ok"


install(JwtPlugin(validation, 'secret'))
run(host="0.0.0.0", port="9988")

