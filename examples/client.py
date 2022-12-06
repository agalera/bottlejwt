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