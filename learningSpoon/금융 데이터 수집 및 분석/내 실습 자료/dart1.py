#Dart 1

import requests
import zipfile
from bs4 import BeautifulSoup
import xmltodict


def get_corp_list():
    API_KEY = "5d28586b7992aa499f241bdd6b79fe35ccb8b732"
    XML_FILE_NAME = "CORPCODE.xml"
    url = "https://opendart.fss.or.kr/api/corpCode.xml"
    params = { "crtfc_key" : API_KEY }

    resp = requests.get(url, params=params)

    f = open("corp_code.zip", "wb") #w : 쓰기모드, b : 바이너리 데이터
    f.write(resp.content) # 서버가 응답을 바이너리 형태인 파일로 주기 때문에 content로 받는다.
    f.close()

    zf = zipfile.ZipFile("corp_code.zip")
    zf.extractall() #zip file 안에 들어있는 모든 데이터를 같은 경로에 압축해제함
    zf.close()

    f = open(XML_FILE_NAME, encoding="utf-8")
    data = f.read()
    f.close()

    """
    #Soup을 사용해서 xml을 파싱하는건 너무 시간이 오래걸림
    soup = BeautifulSoup(data, "html5lib")
    result = soup.select("corp_code")
    
    for item in result[:5]: #너무 많으니 5개만 출력
        print(item.text)
    """

    result = xmltodict.parse(data)
    corp_code = []

    for item in result["result"]["list"][:5]:
        corp_code.append(item["corp_code"])
    return corp_code

corp_code = get_corp_list()

for item in corp_code:
    print(item)