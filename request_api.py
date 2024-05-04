import requests
import json
import os
import argparse
from dotenv import load_dotenv

load_dotenv(verbose=True)


BASE_URL = "https://openapi.ebestsec.co.kr:8080"
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    
class getTRInfo():
    """
    이베스트 api에 조회할 수 있는 모든 종목 정보 확인 
    호가 정보를 위한 api request 보낼 때, 해당 종목의 shcode가 필요한데, 이를 조회하기 위해 사용
    """
    def __init__(self):
        self.path = "stock/etc"
        self.url = f"{BASE_URL}/{self.path}"
    
    def requestInfo(self):
        """
        전체 종목에 대한 정보를 얻는 request 함수
        input: X
        output: 전체 종목에 대한 정보 ('hname', 'shcode', 'expcode, 'etfgubun', 
        'uplmtprice', 'dnlmtprice', 'jnilclose', 'memedan', 'recprice', 'gubun', 
        'bu12gubun', 'spac_gubun') - list 형식으로 출력
        """
        header = {  
            "content-type":"application/json; charset=utf-8", 
            "authorization": f"Bearer {ACCESS_TOKEN}",
            "tr_cd":"t8436",
            "tr_cont":"N",
            "tr_cont_key":"",
        }

        requset = requests.post(self.url, headers=header)
        self.data = requset.json()['t8436OutBlock']
        return self.data
    
    def searchByName(self, data: list, name: list) -> list:
        """
        해당 종목명과 mapping되는 shcode들
        input: requestInfo 로 얻어진 종목 정보 (data), 찾고자 하는 종목 이름 (name)
        output: 해당 종목명과 mapping되는 shcode (list)
        """
        filtered_data = [{'shcode': entry['shcode'], 'hname': entry['hname'], 'expcode': entry['expcode']} for entry in data if entry['hname'] in name]
        return filtered_data

    def searchByExpCode(self, data: list, code: list) -> list:
        """
        해당 종목 코드와 mapping되는 shcode들
        input: requestInfo 로 얻어진 종목 정보 (data), 찾고자 하는 종목 코드 (code)
        output: 해당 종목 코드와 mapping되는 shcode (list)
        """
        filtered_data = [{'shcode': entry['shcode'], 'hname': entry['hname'], 'expcode': entry['expcode']} for entry in data if entry['expcode'] in code]
        return filtered_data
    
    def searchByShcode(self, data: list, shcode: list) -> list:
        """
        해당 shcode와 mapping되는 종목명과 종목코드 (역으로 종목 정보를 찾기 위해)
        input: requestInfo 로 얻어진 종목 정보 (data), 찾고자 하는 shcode (shcode)
        output: 해당 shcode와 mapping되는 종목명과 종목 코드 (list)
        """
        filtered_data = [{'shcode': entry['shcode'], 'hname': entry['hname'], 'expcode': entry['expcode']} for entry in data if entry['shcode'] in shcode]
        return filtered_data

def main(debug=False):
    info = getTRInfo()
    data = info.requestInfo()
    if debug: # 만일 debug mode라면, 예시 코드 실행
        result1 = info.searchByName(data, ["삼성전자", "현대차"])
        result2 = info.searchByExpCode(data, ["KR7005930003", "KR7005930003"])
        result3 = info.searchByShcode(data, ["005930", "005930"])
        print(result1)
        print(result2)
        print(result3)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='debug flag')
    parser.add_argument('--debug', dest='debug', action='store_true', help='Run in debug mode')
    args = parser.parse_args()
    main(args.debug)

    # debug mode로 작동하기 위해서: python request_api.py --debug
    # debug mode 없이 그냥 작동하기 위해서: python request_api.py