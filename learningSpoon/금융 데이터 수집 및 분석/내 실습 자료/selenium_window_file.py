from selenium import webdriver

driver = webdriver.Chrome('/Users/user/Desktop/파이썬 강의/금융 데이터 수집 및 분석/내 실습 자료/chromedriver')

"""
-창전환-

#메인 페이지의 주가 추이 이미지 클릭해서 팝업 띄우고, 팝업에서 전일종가 가져와서 출력 후 팝업닫음. 

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "http://comp.fnguide.com/"
driver.get(url)

selector = "#svdMainChart11 > a"
ui = driver.find_element_by_css_selector(selector)
ui.click()
driver.switch_to.window( driver.window_handles[-1] ) #최근에 열었던 팝업창(-1)을 바라봐

selector = "#chartDataGrid > table > tbody > tr.rwf > td:nth-child(2)"
wait = WebDriverWait(driver, 10)
data = (By.CSS_SELECTOR, selector)
ui = wait.until( EC.presence_of_element_located( data ) )

print(ui.text)

driver.close() # 팝업창 닫음, window_handles에 팝업창 handle 지워짐
driver.switch_to.window( driver.window_handles[-1] ) # 메인 페이지가 -1 인덱스에 저장되어 있게 됨(0을 넣어도됨.) -> 다시 메인페이지로 다시 돌아와
"""


"""
-파일 다루기-
"""

import time

def get_business_summary(driver, ticker):
    url = f"http://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A{ticker}&cID=&MenuYn=Y&ReportGB=&NewMenuID=11&stkGb=&strResearchYN="
    driver.get(url)
    selector = "#bizSummaryHeader"
    ui = driver.find_element_by_css_selector(selector)

    return ui.text


tickers = [ "005930", "000660" ]
#file = open("out.txt", "w")
file = open("out.csv", "w", encoding="cp949")

for ticker in tickers:
    summary = get_business_summary(driver, ticker)
    #file.write(f"{ticker} {summary}" + "\n") #.txt용
    file.write(f"{ticker}, {summary}" + "\n") #엑셀은 셀 seperator가 ',' 이다.
    time.sleep(1) #웹 서버 과부하 방지를 위한 wait
