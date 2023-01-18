import time
import json
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

with open('settings.json') as f:
    json_object = json.load(f)

url = 'https://benedu.co.kr/'
uid = json_object['uid']
upw = json_object['upw']

chrome_path ='chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("lang=ko_KR") # 한국어
chrome_options.add_argument('window-size=1920x1080')

def job():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(url)
    driver.implicitly_wait(3)

    loginId = driver.find_element(By.CSS_SELECTOR, '#loginID')
    loginPw = driver.find_element(By.CSS_SELECTOR, '#loginPW')
    loginId.send_keys(uid)
    loginPw.send_keys(upw)

    driver.find_element(By.CSS_SELECTOR, 'body > section > div.wrap > div.container.right > form > div > div.login-buttons > button:nth-child(1)').click()

schedule.every().day.at('10:30').do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)