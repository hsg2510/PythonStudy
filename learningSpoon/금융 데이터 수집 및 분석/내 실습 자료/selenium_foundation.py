from selenium import webdriver

driver = webdriver.Chrome('/Users/user/Desktop/파이썬 강의/금융 데이터 수집 및 분석/내 실습 자료/chromedriver')
driver.get('http://naver.com')

"""
selector = "#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li:nth-child(9) > a"
ui = driver.find_element_by_css_selector(selector)
ui.click() #네이버 웹툰 이동

selector = "#content > div:nth-child(3) > ul > li:nth-child(2) > ul > li:nth-child(1) > div.genreRecomInfo > h6 > a"
ui = driver.find_element_by_css_selector(selector)
ui.click() #특정 만화 페이지 이동
"""

"""
#검색창에 "러닝스푼즈" 입력하고 검색
selector = "#query"
ui = driver.find_element_by_css_selector(selector)
ui.send_keys("러닝스푼즈")

selector = "#search_btn"
ui = driver.find_element_by_css_selector(selector)
ui.click()
"""