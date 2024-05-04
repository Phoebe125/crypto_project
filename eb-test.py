import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)


BASE_URL = "https://openapi.ebestsec.co.kr:8080"
PATH = "stock/market-data"
URL = f"{BASE_URL}/{PATH}"
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")


header = {  
    "content-type":"application/json; charset=utf-8", 
    "authorization": f"Bearer {ACCESS_TOKEN}",
    "tr_cd":"t1101", 
    "tr_cont":"N",
    "tr_cont_key":"",
}

body = {
    "t1101InBlock" : 
    {    
        "shcode" : "078020",    
    }
}

requset = requests.post(URL, headers=header, data=json.dumps(body))
print(requset.json()['t1101OutBlock'])
