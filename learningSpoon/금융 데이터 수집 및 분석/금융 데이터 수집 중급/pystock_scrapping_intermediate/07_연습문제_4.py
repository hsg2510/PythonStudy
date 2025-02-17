import requests
from bs4 import BeautifulSoup

def get_report_info(시작일, 종료일, 리포터) :
    url = "http://consensus.hankyung.com/apps.analysis/analysis.list"

    params = {
        "sdate":시작일,
        "edate": 종료일,
        "now_page":1,
        "report_type":"CO",
        "pagenum":20,
        "search_text": 리포터.encode('euc-kr')
    }

    headers = {
        "User-Agent": "Hi"
    }

    resp = requests.get(url, headers=headers, params=params)
    resp.encoding = 'euc-kr'
    soup = BeautifulSoup(resp.text, 'html5lib')

    일자 = [ ]
    sel = "#contents > div.table_style01 > table > tbody > tr > td:nth-child(1)"
    result = soup.select(sel)
    for item in result:
        일자.append(item.text.strip())

    제목 = [ ]
    sel = "#contents > div.table_style01 > table > tbody > tr > td:nth-child(2)"
    result = soup.select(sel)
    for item in result:
        제목.append(item.text.strip())

    투자의견 = []
    sel = "#contents > div.table_style01 > table > tbody > tr > td:nth-child(4)"
    result = soup.select(sel)
    for item in result:
        투자의견.append(item.text.strip())

    return [  일자, 제목, 투자의견  ]

def get_earning_rate (ticker, open_year, open_mon, open_day):
    url = f"http://consensus.hankyung.com/apps.chart/chart.chartList?report_type=CO&business_code={ticker}"
    headers = {"user-agent": "hi"}
    resp = requests.get(url, headers=headers)
    r = resp.text

    r = r.replace("[,", "")
    r = r.replace(" \n", "")
    r = r.replace("jQuery112407887789095301501_1590834572386", "")
    r = r.replace("Date.UTC", "")
    r = r.replace("[", "")
    r = r.replace("]", "")
    r = r.replace("(", "")
    r = r.replace(")", "")
    r = r.replace('null', '0')
    r = r.split(",")
    for i in range(0, len(r), 4):
        year = int(r[i])
        mon = int(r[i+1]) + 1
        day = int(r[i+2]) - 1
        val = int(r[i+3])

        if year == open_year and mon == open_mon and day == open_day :
            시가 = val
            종가 = int(r[-1])
            return (종가 / 시가 - 1) * 100



def print_earning_rate(시작일, 종료일, reporter):
    result = get_report_info(시작일, 종료일, reporter)
    for idx in range( len(result[0]) ) :

        if result[2][idx] != "Buy" :
            continue

        제목 = result[1][idx]

        if '(' not in 제목:
            continue

        start_index = 제목.index('(')
        ticker = 제목[start_index+1 : start_index+7 ]
        open_year = int(result[0][idx][:4])
        open_mon  = int(result[0][idx][5:7])
        open_day  = int(result[0][idx][8:10])

        수익률 = get_earning_rate(ticker, open_year, open_mon, open_day)
        print(ticker, 수익률)


print_earning_rate('2020-01-01', '2020-01-20', '최준영')
print_earning_rate('2020-01-01', '2020-01-20', '김평모')
print_earning_rate('2020-01-01', '2020-01-20', '신은정')
print_earning_rate('2020-01-01', '2020-01-20', '주영훈')











