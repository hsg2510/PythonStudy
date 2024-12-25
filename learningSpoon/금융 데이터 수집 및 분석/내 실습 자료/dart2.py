

#Dart 2(공시 검색)

import requests
from bs4 import BeautifulSoup

def get_report_info(start_date, corp_code):
    API_KEY = "5d28586b7992aa499f241bdd6b79fe35ccb8b732"
    url = "https://opendart.fss.or.kr/api/list.json"
    params = { "crtfc_key" : API_KEY,
               "corp_code" : corp_code,
               "bgn_de" : start_date,
               "pblntf_ty" : "A", #정기공시정보만 검색
               "corp_cls" : "Y",
               "page_no" : 1,
               "page_count" : 10 }

    resp = requests.get(url, params=params)

    resp = requests.get(url, params=params)
    data = resp.json()
    rcept_no = []
    for item in data["list"]:
        #print(item["corp_name"], item["report_nm"], item["rcept_no"])
        rcept_no.append(item["rcept_no"])

    return rcept_no


#공시보고서 내 검색
url = "http://m.dart.fss.or.kr/html_mdart/MD1007.html?rcpNo=20200814001766"
resp = requests.get(url)
#print("186,136,845" in resp.text) #원하는 데이터 있는지 확인
#print("186136845" in resp.text) #서버가 "," 제거하고 반환할 수 있으니
#둘다 false -> 개발자 도구 켜서 F5후 직접 검색

def 유동자산(rcept_no, dcmNo, eleId):
    url = "http://m.dart.fss.or.kr/report/main.do"
    headers = {
        "User-Agent" : "hi"
    }
    data = {
        "rcpNo" : rcept_no,
        "dcmNo" : dcmNo,
        "eleId" : eleId
    }
    resp = requests.post(url, headers=headers, data=data)
    #print("186,136,845" in resp.text)

    soup = BeautifulSoup(resp.text, "html5lib")
    sel = "tr:nth-child(2) > td:nth-child(2)"
    result = soup.select(sel)
    print(result[0].text.strip())

유동자산("20200814001766", "7446167", "12")

#그럼 유동자산()의 2, 3번째 param인 dcmNo, eleId는 어디서 얻어오지? -> 개발자 도구에서 "dcmNo" 검색해보자.
def get_dcmno_and_eleid(rcpNo):
    url = f"http://m.dart.fss.or.kr/viewer/main.st?rcpNo={rcpNo}&dcmNo=&_=1598970425995"
    resp = requests.get(url)
    data = resp.json()
    #print(data) #eleId = 12와 dcmNo = 7446167인 곳을 찾아가보자.

    for item in data["toc"]:
        if "재무에 관한 사항" in item["tocText"]:
            for sub_item in item["children"]:
                if ("요약재무정보" in sub_item["tocText"]):
                    return (sub_item["dcmNo"], sub_item["eleId"])

    return None

#result = get_dcmno_and_eleid("20200814001766")
#print(result[0], result[1])


rcept_no = get_report_info("20200101", "00126380")

for no in rcept_no:
    result = get_dcmno_and_eleid(no)
    유동자산(no, result[0], result[1])
