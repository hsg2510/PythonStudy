import requests


####웹페이지 분석####

"""
개발자 도구 - network

항목을 선택하면 상세 내용이 오른쪽에 출력
-Headers: 웹 서버 정보와 입력 데이터 확인 
-Response: 웹 서버가 반환하는 데이터 확인(반환 데이터는 html, json, 문자열 등 다양하다.)
-Network tab의 Preserve log(새 request 요청할때 마다, 이전 요청정보를 안 지우고 계속 나타냄), Disable cache 체크 해놓기 

request의 header는 optional한 정보이다. 
- 요청하는 데이터가 어떤 Type인지 등등의 부가적인 정보가 들어감 
- ":"으로 시작하는 http2 프로토콜에 해당하며, 이를 파이썬 request가 지원하지 않는다. 다행히, 대부분의 웹서버는 ":"이 붙은 정보들은 체크하지 않기 때문에, 
  과감히 생략해도 된다. 
- 웹서버가 어떤 header 정보를 필요로 하는지 아닌지는 알 수 없기 때문에, 일단 모든 header 정보를 넣어서 request 날려보고, 점점 header를 줄여가면서,
  최적화된 request를 찾아야 한다.  
"""


"""
url = "http://finance.daum.net/api/sectors?market=KOSDAQ&change=RISE&includedStockLimit=1&perPage=5"
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "_TI_NID=iok9mjEFfnWoNqMjDA5hheqpwFiBVH/szXJZTO71JqZ2uPIyPk4utnmRmMidM5IQV0pSENwIZe+9p4Dfn73j2w==; _ga=GA1.2.150946550.1598358855; _gid=GA1.2.1415250940.1598358855; KAKAO_STOCK_RECENT=[%22A005930%22]; __T_=1; TIARA=SYINl5.BpX7MHDzZ2rwgRMUznpXGAfOaYsK6k6d5toYk-YFXCZ1uYJoeuvmBjFQ1zjPl3DsK-9aqc5WlNKY7NA00; _dfs=ei9QeFF0Q0tFOHpuVWhoNTVvK0p6OFJzZGZYUDdsVEViLzVVR3pNYi8yK0ZrRjAwN01YcEI1Vzl3L3o0NFRmSjhoamhwWlhzUnRlRWljU2RRa1R4NHc9PS0tdVJtTHVVV1d2YVNHZTF0WDlTYjVQdz09--e93e54c83e6daa19b7b7a9998e3216e3416b7b5a",
    "Host": "finance.daum.net",
    "Pragma": "no-cache",
    "Referer": "http://finance.daum.net/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
resp = requests.get(url, headers=headers)
result = resp.json()

for item in result["data"]:
    print(item["sectorName"])
"""


"""
#연습 문제1 - 카카오 쇼핑하기의 핫딜 최저가 품목의 이름과 가격 스크래핑

# url = "https://shoppinghow.kakao.com/siso/p/api/hotdeal/list?contentseq=&_=1598362532103"
# -> get의 parameter를 따로 뺄 수 있다.
url = "https://shoppinghow.kakao.com/siso/p/api/hotdeal/list"
params = {
    "contentseq" : "",
    "_" : "1598362532103"
}
headers = {
    "Accept" : "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding" : "gzip, deflate, br",
    "Pragma": "no-cache",
    "Referer": "https://shoppinghow.kakao.com/siso/p/hotdeal/list/"
}
resp = requests.get(url, headers=headers, params = params)
result = resp.json()
print(result)
print(result["todayList"][0]["title"], result["todayList"][0]["minPrice"])
"""


"""
#연습문제1 - 카카오 번역 페이지에서 번역된 결과를 받아와라.  

url = "https://translate.kakao.com/translator/translate.json"
headers = {
    "Accept" : "*/*",
    "Accept-Encoding" : "gzip, deflate, br",
    "Pragma": "no-cache",
    "Referer": "https://translate.kakao.com/"
}

data = {
    "queryLanguage" : "kr",
    "resultLanguage" : "en",
    "q" : "사랑합니다"
}
resp = requests.post(url, headers=headers, data=data)

print(resp.json()["result"]["output"][0][0])
"""

 