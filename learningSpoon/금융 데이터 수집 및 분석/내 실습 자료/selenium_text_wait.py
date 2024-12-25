from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/user/Desktop/파이썬 강의/금융 데이터 수집 및 분석/내 실습 자료/chromedriver')

"""
#시가총액 여러개 가져오기
for ticker in ["005930", "066575", "000660"] :
    driver.get('http://finance.naver.com/item/main.nhn?code=' + ticker)
    selector = "#_market_sum"
    ui = driver.find_element_by_css_selector(selector)
    print(ui.text)
    time.sleep(2)
"""

"""
#네이버 금융 홈에서 주요기사 6개 가져오기
#방법1
for index in range(1, 7):
    driver.get('https://finance.naver.com/')
    selector = f"#content > div.article > div.section > div.news_area > div > ul > li:nth-child({index}) > span > a"
    ui = driver.find_element_by_css_selector(selector)
    print(ui.text)

#방법2
driver.get('https://finance.naver.com/')
selector = "#content > div.article > div.section > div.news_area > div > ul > li > span > a" # nth=child 부분 삭제해서 여러개 선택되게 함
ui_list = driver.find_elements_by_css_selector(selector) #element -> elements(리스트로 가져옴)
for web_element in ui_list:
    print(web_element.text)
"""


#Wait
"""
NoSuchElementException -> 니가 지정한 셀렉터에 대응되는 HTML을 찾을 수 없어 발생하는 예외
이 경우는 로딩이 느린 웹페이지에서 빈번하게 발생한다. 
"""

"""
#최대 10초까지 웹페이지의 로딩을 기다림 -> 1초만에 웹페이지 뜨면 다음코드 실행.
driver.implicitly_wait(10) 
driver.get('https://www.investing.com/indices/us-spx-500')
selector = "#leftColumn > div:nth-child(20) > article:nth-child(3) > div.textDiv > a"
ui = driver.find_element_by_css_selector(selector)
print(ui.text)
"""

#특정 조건이 만족할 때 까지 기다림, 보통 implicity_wait 보다 이 코드를 사용한다.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get('https://www.investing.com/indices/us-spx-500')
selector = "#leftColumn > div:nth-child(20) > article:nth-child(3) > div.textDiv > a"
wait = WebDriverWait(driver, 10)
data = (By.CSS_SELECTOR, selector)
ui = wait.until( EC.presence_of_element_located( data ) )
print(ui.text)
"""