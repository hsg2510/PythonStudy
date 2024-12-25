import requests
from bs4 import BeautifulSoup



#네이버 상단 메뉴 리스트 출
url = "https://www.naver.com"
resp = requests.get(url)

bs = BeautifulSoup(resp.text, "html5lib") # "html5lib" html 문서가 약간 문법에 안맞더라도 최대한 결과를 맞춰서 주려고 노력하는 옵션임.
selector = "#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li > a"
result = bs.select(selector)
print(type(result))
#print(type(result[0]))
#print(result[0])
#print(result[0].text)

for item in result:
    print(item.text.strip())



"""
#동적 웹페이지 
# -다수의 웹 서버에서 정보를 가져와 하나의 페이지를 구성
# -웹 브라우저로 특정 url로 이동을 하면, 브라우저는 이 url로 request 날림, 이 웹서버에서 처리가 가능한 데이터는 바로 response줌, 그러나      
#  다른 웹 서버에서 데이터를 가져와야 되는 경우, 다른 웹서버로 request 날리고, response를 받아 웹 브라우저에 랜더링 함  
#  즉, 셀레늄으로 처리할 때는 동적 웹페이지 처리도 문제가 없었지만, BeatifulSoup은 특정 URL로 request를 날리고 그에 해당하는 response만 받아서 처리 
#  하는 구조라, 동적 웹페이지 처리에는 문제가 생김.
"""

"""
#정적 웹페이지 라고 하더라도 웹 브라우저에서 url 이동 후 셀렉터 가져와서 조회해 보면 데이터가 안나올때가 있다. 
#이런 경우 BeautifulSoup로 request 날려서 html 가져오고 이거를 .html 파일 저장 후 연 다음에 셀렉터를 다시 검색해서 적용해야 한다. 
#웹서버가 응답해주는 response는 동일 하지만, 웹 브라우저 자체에서 데이터를 자체 변경하는 경우다. 이런 경우는 흔하니 주의 바란다. 
#그리고 셀렉터에 대해 완벽히 이해 했다면, 불필요한 셀렉터 구문을 지워서 셀렉터를 간략하게 할 수도 있다.  
"""