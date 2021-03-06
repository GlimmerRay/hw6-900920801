import requests
from credentials import client_id, client_secret

scope = 'code'
token_endpoint = 'https://accounts.spotify.com/api/token'
grant_type = 'client_credentials'

token_params = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
}

def get_access_token():
    return requests.post(token_endpoint, token_params).json()['access_token']

def print_new_releases():
    access_token = get_access_token()
    print(access_token, 'access_token')
    endpoint = 'https://api.spotify.com/v1/browse/new-releases'
    headers = {
        'access_token': access_token
    }
    items = requests.get(endpoint, headers).json()['albums']['items']
    for i in range(10):
        print(items[i]['name'])

print_new_releases()