import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

BASE_URL = "https://openapi.ebestsec.co.kr:8080"
PATH = "oauth2/token"
URL = f"{BASE_URL}/{PATH}"
APP_KEY = TELEGRAM_TOKEN = os.getenv('APPKEY')
APP_SECRET = TELEGRAM_TOKEN = os.getenv('APPSECRET')

header = {"content-type":"application/x-www-form-urlencoded"}
param = {"grant_type":"client_credentials", "appkey":APP_KEY, "appsecretkey":APP_SECRET,"scope":"oob"}


request = requests.post(URL, verify=False, headers=header, params=param)
ACCESS_TOKEN = request.json()["access_token"] 
print(ACCESS_TOKEN)