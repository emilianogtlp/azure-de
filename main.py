import os
from dotenv import load_dotenv
import requests

load_dotenv()

key = os.environ.get('CLIENT_ID')
secret = os.environ.get('SECRET_KEY')
emiliano_pass = os.environ.get('EMILIANO')

auth = requests.auth.HTTPBasicAuth(key,secret)

data = {
    'grant_type':'password',
    'username':'emilianogtlp',
    'password':emiliano_pass
}

headers = {'User-Agent':'de-medium/0.0.1'}
res = requests.post('https://reddit.com/api/v1/access_token',auth=auth,data=data,headers=headers)
print(res.json())