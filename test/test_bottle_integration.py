from webtest import TestApp
import server
from bottlejwt import JwtPlugin
import unittest


app = TestApp(server.app[0])
pluginjwt = JwtPlugin(False, 'secret', algorithm='HS256')
valid_token = JwtPlugin.encode({'name': 'pepito', 'auth': 1})
invalid_token_1 = JwtPlugin.encode({'name': 'pepito', 'auth': 0})
invalid_token_2 = JwtPlugin.encode({'name': 'pepito'})
invalid_token_3 = "random text"


class TestMethods(unittest.TestCase):
    def test_authenticate_valid_token_url_arg(self):
        r = app.get('/authenticate?access_token=%s' % valid_token)
        assert r.status_code == 200

    def test_authenticate_valid_token_header(self):
        headers1 = {'Authorization': 'bearer %s' % valid_token}
        r1 = app.get('/authenticate', headers=headers1)
        assert r1.status_code == 200

        headers2 = {'Authorization': 'Bearer %s' % valid_token}
        r2 = app.get('/authenticate', headers=headers2)
        assert r2.status_code == 200

    def test_authenticate_valid_token_header_without_type_bearer(self):
        headers = {'Authorization': valid_token}
        r = app.get('/authenticate', headers=headers,
                    expect_errors=True)
        assert r.status_code == 403

        headers = {'Authorization': 'naranjas %s' % valid_token}
        r = app.get('/authenticate', headers=headers,
                    expect_errors=True)
        assert r.status_code == 403

    def test_authenticate_no_token(self):
        r = app.get('/authenticate',
                    expect_errors=True)
        assert r.status_code == 403

    def test_authenticate_invalid_token(self):
        # validation error (auth != 1)
        r1 = app.get('/authenticate?access_token=%s' % invalid_token_1,
                     expect_errors=True)
        assert r1.status_code == 401

        # validation error (no content auth)
        r2 = app.get('/authenticate?access_token=%s' % invalid_token_2,
                     expect_errors=True)
        assert r2.status_code == 401

        # token invalid
        r3 = app.get('/authenticate?access_token=%s' % invalid_token_3,
                     expect_errors=True)
        assert r3.status_code == 403

    def test_authenticate_valid_token_without_argument(self):
        r = app.get('/authenticate_without_argument?access_token=%s' %
                    valid_token)
        assert r.status_code == 200

    def test_without_authenticate(self):
        r = app.get('/without_authenticate')
        assert r.status_code == 200


if __name__ == '__main__':
    unittest.main()
