

"""
네이버 금융 페이지를 스크래핑 해서 데이터 베이스로 구성하기
"""

import requests
from bs4 import BeautifulSoup
import sqlite3
import time

"""
con = sqlite3.connect("samplerPrj.db")
cur = con.cursor()
query = "create table if not exists ticker ( ticker text, name text )"
cur.execute(query)

url = "https://finance.naver.com/sise/sise_market_sum.nhn"
headers = { "User-Agent" : "hi" }
resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.text, "html5lib")
#종목명의 selector를 가져
#selector = "#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(2) > td:nth-child(2) > a"
# "Only the following pseudo-classes are implemented: nth-of-type."
# python 버전에 따라 이런 에러가 날 수도 있는데 -? "nth-child" 를 "nth-of-type" 으로 변경해주면 된다.
selector = "#contentarea > div.box_type_l > table.type_2 > tbody > tr > td:nth-child(2) > a"
result = soup.select(selector)

for item in result:
    ticker = item["href"].split("=")[1] #/item/main.nhn?code=005930 여기에서 005930 뽑아옴
    name = item.text
    print(ticker, name)
    query = f"insert into ticker values( '{ticker}', '{name}' )"
    cur.execute(query)

con.commit()
con.close()
"""

"""특정종목의 per, pbr, 배당수익률 가져오기"""
def getInfoFromSel(selector, html):
    soup = BeautifulSoup(html, "html5lib")
    result = soup.select(selector)

    return result[0].text

def convertFloatFromStr(str):
    try:
        return float(str)
    except:
        return 0.0

def getStockInfo(ticker):
    result = {}
    url = f"https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd={ticker}"
    headers = {"User-Agent": "hi"}
    response = requests.get(url, headers=headers)
    per_selector = "#pArea > div.wrapper-table > div > table > tbody > tr:nth-child(3) > td > dl > dt:nth-child(3) > b"
    result["per"] = convertFloatFromStr(getInfoFromSel(per_selector, response.text))
    pbr_selector = "#pArea > div.wrapper-table > div > table > tbody > tr:nth-child(3) > td > dl > dt:nth-child(5) > b"
    result["pbr"] = convertFloatFromStr(getInfoFromSel(pbr_selector, response.text))
    div_selector = "#pArea > div.wrapper-table > div > table > tbody > tr:nth-child(3) > td > dl > dt:nth-child(6) > b"
    result["div"] = convertFloatFromStr(getInfoFromSel(div_selector, response.text).replace("%", ""))

    return result

con = sqlite3.connect("samplerPrj.db")
cur = con.cursor()
query = "select * from ticker"
cur.execute(query)

tickers = cur.fetchall()

for t in tickers:
    ticker = t[0]
    result = getStockInfo(ticker)
    time.sleep(1.0)
    print(result)

con.commit()
con.close()