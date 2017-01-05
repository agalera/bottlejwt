import unittest
from bottlejwt import JwtPlugin


class TestMethods(unittest.TestCase):
    def test_create_and_decode_token(self):
        # is a singleton, you only need to initialize once.
        # * If you did install() also work
        self.pluginjwt = JwtPlugin(False, 'secret', algorithm='HS256')
        new_token = JwtPlugin.encode({'name': 'pepito'})
        self.assertEqual({'name': 'pepito'}, self.pluginjwt.decode(new_token))


if __name__ == '__main__':
    unittest.main()
