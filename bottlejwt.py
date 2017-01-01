from bottle import request, HTTPError
import inspect
from functools import wraps
import jwt


class JwtPlugin(object):
    name = 'JwtPlugin'
    api = 2
    keyword = 'auth'

    def __init__(self, validation, key, algorithm="HS512",
                 headers=None, json_decoder=None):
        JwtPlugin.jwt = {'key': key,
                         'algorithm': algorithm,
                         'headers': headers,
                         'json_decoder': json_decoder}
        self.validation = validation

    @classmethod
    def encode(self, data):
        kwargs = JwtPlugin.jwt.copy()
        del kwargs['json_decoder']
        return jwt.encode(data, **kwargs).decode('utf-8')

    def decode(self, data):
        try:
            return jwt.decode(data, **JwtPlugin.jwt)
        except:
            return None

    def get_token(self):
        try:
            token = request.query.get('access_token', None)
            if token:
                return token
            _type, token = request.headers['Authorization'].split(" ")
            if _type.lower() != "bearer":
                return None
            return token
        except:
            return None

    def get_auth(self):
        token = self.get_token()
        if not token:
            raise HTTPError(403, "Forbidden")
        decoded = self.decode(token)
        if decoded is None:
            raise HTTPError(403, "Forbidden, bad token")
        decoded['token'] = token
        return decoded

    def apply(self, callback, route):
        auth_value = route.config.get(self.keyword, None)
        if not auth_value:
            return callback

        @wraps(callback)
        def wrapper(*args, **kwargs):
            auth = self.get_auth()
            if self.validation(auth, auth_value):
                if inspect.signature(callback).parameters.get(self.keyword):
                    kwargs['auth'] = auth
                return callback(*args, **kwargs)
            else:
                raise HTTPError(401, "Unauthorized")
        return wrapper
