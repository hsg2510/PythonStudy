

#연습문제-3 : 한경 차트 데이터 스크래핑
#html, json도 아닌 불필요한 정보가 포함된 문자열로 넘어올 때.

import requests
from bs4 import BeautifulSoup

#에치에프알
#url = "http://consensus.hankyung.com/apps.chart/chart.chartList?callback=jQuery112408402551867592534_1598872031800&report_type=CO&business_code=230240&_=1598872031801"
#sk하이닉스
#url = "http://consensus.hankyung.com/apps.chart/chart.chartList?callback=jQuery112408402551867592534_1598872031800&report_type=CO&business_code=000660&_=1598872031801"
# 두개 비교해보니, business_code와, callback이 다르다. business_code만 변경해도 제대로 값 넘어옴.  -> callback은 의미가 없나? -> 하나씩 제거해보니
url = "http://consensus.hankyung.com/apps.chart/chart.chartList?report_type=CO&business_code=000660" # 이 정도만 있어도 데이터 얻을 수 있음
headers = {
    "user-agent" : "hi"
}

resp = requests.get(url, headers=headers)
r = resp.text
r = r.replace(" \n", "")
r = r.replace("jQuery112408402551867592534_1598872031800", "")
r = r.replace("[", "")
r = r.replace("]", "")
r = r.replace("(", "")
r = r.replace(")", "")
r = r.replace("Date.UTC", "")
r = r.replace('null', '0') # 서버에서 잘못된 값을 줄수 있음, 이 경우 밑에서 int로 형 변환할때 에러가 남
r = r.split(",")

for i in range(0, len(r), 4): #index 4씩 증가
    year = int(r[i])
    mon = int(r[i+1]) + 1 # 월이 0부터 시작함
    day = int(r[i+2]) - 1 #일이 2부터 시작함
    val = int(r[i+3])

    print(year, mon, day, val)
