import os
from dotenv import load_dotenv
import requests
import requests.auth

def get_token():
    load_dotenv()

    key = os.environ.get('CLIENT_ID')
    secret = os.environ.get('SECRET_KEY')
    emiliano_pass = os.environ.get('EMILIANO')

    client_auth = requests.auth.HTTPBasicAuth(key,secret)

    data = {
        'grant_type':'password',
        'username':'emilianogtlp',
        'password':emiliano_pass
    }

    headers = {'User-Agent':'de-medium 0.0.1'}

    try:
        response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=data, headers=headers)
        response.raise_for_status() # Raise an exception if the response status code is not 2xx
    
    except (requests.exceptions.RequestException, ValueError) as err:
        print(f"An error occurred while fetching the access token: {err}")
        return None

    access_token = response.json().get('access_token')
    if access_token is None:
        print("Unable to get access token from Reddit API")
        return None
    
    return access_token
        