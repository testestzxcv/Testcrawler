import time
from konlpy.tag import Twitter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pymysql

# 사이트주소=https://www.standard.go.kr/KSCI/crtfcInsttPot/searchCrtfcInsttPotList.do

url = 'https://www.standard.go.kr/KSCI/crtfcInsttPot/searchCrtfcInsttPotList.do'

DRIVER_DIR = './chromedriver/chromedriver_win.exe'

driver = webdriver.Chrome(DRIVER_DIR)

# driver.implicitly_wait(2)

driver.get(url)

for i in range(30):
    if i >= 10:
        if (i % 10)==0:
            e = driver.find_element_by_css_selector(
                '#crtfcInsttPotVO > div > div.page > div > ul > li.next > a')
            print("다음버튼")
            e.click()
    e = driver.find_element_by_css_selector(
        '#crtfcInsttPotVO > div > div.page > div > ul > li:nth-child({}) > a'.format((i % 10) + 3))
    print("{} 클릭".format(i))
    e.click()
    products = driver.find_elements_by_css_selector('#crtfcInsttPotVO > div > div.table.list > table > tbody > tr')
    for product in products:
        print("-", product.text)



