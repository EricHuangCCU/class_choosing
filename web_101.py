from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
from datetime import datetime


chrome_options = Options() # 啟動無頭模式
chrome_options.add_argument('--headless')  #規避google bug
chrome_options.add_argument('--disable-gpu')

PATH = "C:/Users/88690/python_code/chromedriver.exe" #改
#driver = webdriver.Chrome(executable_path=PATH,chrome_options=chrome_options)
driver = webdriver.Chrome(PATH)
driver.get("https://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class_new/")



#time.sleep(2)
driver.switch_to.frame('bookmark')
ID = driver.find_element_by_name('id')
PASSWORD = driver.find_element_by_name('password')
BUTTON = driver.find_element_by_xpath('/html/body/font/center/form/table/tbody/tr[6]/td/input[1]')
ID.clear()
PASSWORD.clear()

#time.sleep(2)

ID.send_keys('id')
PASSWORD.send_keys('passwd')
BUTTON.click()

ADD_BUTTON = driver.find_element_by_xpath('//*[@id="itemTextLink4"]')
ADD_BUTTON.click()

driver.switch_to.default_content()
driver.switch_to.frame('basefrm')

CENTER_BUTTON = driver.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[8]/font/input[3]')
CENTER_BUTTON.click()
BOYA_BUTTON = driver.find_element_by_xpath('//*[@id="cge_cate2"]')
BOYA_BUTTON.click()
SIX_BUTTON = driver.find_element_by_xpath('//*[@id="cge_subcate2"]/input[7]')
SIX_BUTTON.click()
CHECK_BUTTON = driver.find_element_by_xpath('//*[@id="form1"]/input[6]')
CHECK_BUTTON.click()


#/html/body/center/form/table/tbody/tr[4]/th[1]/form/a[1]
NEW_PAGE_BUTTON = driver.find_element_by_xpath('/html/body/center/form/table/tbody/tr[4]/th[1]/form/a[1]')
NEW_PAGE_BUTTON.click()

#body > center > form > table > tbody > tr:nth-child(1) > th > table > tbody > tr:nth-child(9) > th:nth-child(4) > font
while True:
    CLASS_NUM_2 = driver.find_element_by_css_selector('tr:nth-child(8) > th:nth-child(4)')
    currentDateAndTime = datetime.now()
    #body > center > form > table > tbody > tr:nth-child(1) > th > table > tbody > tr:nth-child(8) > th:nth-child(4) > font
    print(CLASS_NUM_2.text," ",currentDateAndTime)

    if CLASS_NUM_2.text == "0":
        #/html/body/center/form/table/tbody/tr[4]/th[1]/form/a[1]
        FIRST_PAGE_BUTTON = driver.find_element_by_xpath('/html/body/center/form/table/tbody/tr[3]/th[1]/form/a[1]')
        FIRST_PAGE_BUTTON.click()
        
        SECOND_PAGE_BUTTON = driver.find_element_by_xpath('/html/body/center/form/table/tbody/tr[4]/th[1]/form/a[1]')
        SECOND_PAGE_BUTTON.click()
       
    else:
        #/html/body/center/form/table/tbody/tr[1]/th/table/tbody/tr[9]/th[1]/input
        headers = {
        "Authorization": "Bearer " + "MvVlqF6SfTCYwa0RxuMlwaCMx94Tq9BFfcOtyoFXbd8",
        "Content-Type": "application/x-www-form-urlencoded"
        }
        params = {"message": "星空101有課uwu"}
        r = requests.post("https://notify-api.line.me/api/notify",headers=headers, params=params)

        CHOOSE_COURSE_BUTTON = driver.find_element_by_xpath('/html/body/center/form/table/tbody/tr[1]/th/table/tbody/tr[8]/th[1]/input')
        CHOOSE_COURSE_BUTTON.click()
        COFIRM_BUTTON = driver.find_element_by_xpath('/html/body/center/form/table/tbody/tr[2]/th/input')
        COFIRM_BUTTON.click()
        break
        