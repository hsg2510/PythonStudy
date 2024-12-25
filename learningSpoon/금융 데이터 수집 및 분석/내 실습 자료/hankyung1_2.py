

"""
#안코딩과 디코딩
#ASCII - 영어, 숫자, 특수문자 등 128개의 문자를 표현
#EUC-KR - 2350 글자의 한글 표현(이 갯수 만으로도 모든 한글 표현 못함)
#CP949 - 11172 글자의 한글 표현(한글은 다 표현)
#유니코드 - 한글 뿐만 아니라 유럽, 일본 등의 전 세계 모든 문자를 표현(UTF-8도 유니코드 종류의 한 가지다.)

문자 = "안녕"
euc = 문자.encode("euc-kr")
print(euc)
euc = euc.decode("euc-kr")
print(euc)

cp = 문자.encode("cp949")
print(cp)
cp = cp.decode("euc-kr")
print(cp)

utf8 = 문자.encode("utf-8")
print(utf8)
utf8 = utf8.decode("utf-8")
print(utf8)

"""

#한경 컨센서스1

"""연습문제1 - 기업의 report 제목, 적정가격, 투자의견을 출력."""
import requests
from bs4 import BeautifulSoup

def get_items(resp, nth):
    soup = BeautifulSoup(resp.text, "html5lib")
    selector = f"#contents > div.table_style01 > table > tbody > tr > td:nth-child({str(nth)})"
    result = soup.select(selector)

    list_result = []
    for item in result:
        list_result.append(item.text.strip())

    return list_result
"""
url = "http://consensus.hankyung.com/apps.analysis/analysis.list?&skinType=business"
headers = {
    "User-Agent": "Mozilla/5.0"
}
resp = requests.get(url, headers=headers)

일자_리스트 = get_items(resp, 1)
제목_리스트 = get_items(resp, 2)
적정가격_리스트 = get_items(resp, 3)

for idx in range( len(일자_리스트) ):
    print(f"작성일 : {일자_리스트[idx]} 제목 : {제목_리스트[idx]} 적정가격 : {적정가격_리스트[idx]}")
    # 제목이 깨짐, 옛날에 만든 웹페이지 같은 경우에는 과거에 많이 사용했던 인코딩 방식으로 한글을 저장해놈, 대부분의 웹사이트는 유니코드를 사용할 텐데,
    # 유니코드를 사용하지 않는다면 다음과 같이 깨진다.
    # "euc-kr", "cp949", "utf-8" 등을 넣어봐라.
"""

url = "http://consensus.hankyung.com/apps.analysis/analysis.list?&skinType=business"
headers = {
    "User-Agent": "Mozilla/5.0"
}
resp = requests.get(url, headers=headers)
resp.encoding = "euc-kr" # 이렇게 encoding을 설정하면, resp.text를 반환할 때, 지정한 encoding 방식으로 decoding 해서 return 해줌.

일자_리스트 = get_items(resp, 1)
제목_리스트 = get_items(resp, 2)
적정가격_리스트 = get_items(resp, 3)

for idx in range( len(일자_리스트) ):
    print(f"작성일 : {일자_리스트[idx]} 제목 : {제목_리스트[idx]} 적정가격 : {적정가격_리스트[idx]}")
    #제목에 포함된 ticker를 뽑아보자. -> 현대차(005380) 이런식임
    제목 = 제목_리스트[idx]

    if ("(" not in 제목): #제목.index("(") 에서 제목 문자열 안에 "("이 없으면 Value Error를 내뱉게 된다.
        continue
    start_index = 제목.index("(")
    ticker = 제목[start_index + 1 : start_index + 7]
    print("ticker : " + ticker)

"""
#param에 인코딩 된 문자열 넣어야 할때.
url = "http://consensus.hankyung.com/apps.analysis/analysis.list"
params = {
    "sdate" : "2020-07-31",
    "edate" : "2020-08-31",
    "&now_page" : "1",
    "report_type" : "CO",
    "pagenum" : "20",
    # "search_text" : "%C3%D6%C1%D8%BF%B5", 원래는 이렇게 입력되어 있었음 -> url 표시창에 한글로 "최준영" 이라고 적고 검색해봄 -> 안됨.
    # -> 아 param을 보낼때 인코딩 해서 보내야 되는구나.
    "search_text" : "최준영".encode("euc-kr")

}
headers = {
    "User-Agent": "Mozilla/5.0"
}
resp = requests.get(url, headers=headers, params=params)
print(resp.encoding) # 웹서버가 ISO-8859-1를 사용해서 데이터를 인코딩 했다라고 알려주고 있는것. -> 한글을 인코딩 할 수 있는 형식이 아님.
#-> 즉, euc-kr 이나 한글 인코딩이 가능한 다른 옵션으로 인코딩 해놓고, 잘못된 정보를 알려준것.

resp.encoding = "euc-kr" # 이렇게 encoding을 설정하면, resp.text를 반환할 때, 지정한 encoding 방식으로 decoding 해서 return 해줌.
print(resp.text)
"""