#!/usr/local/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=chrome_options)

def set_cookies(driver, raw_cookies):
    for raw_cookie in raw_cookies.split("; "):
        cookie = raw_cookie.split("=")
        driver.add_cookie({
            'name': cookie[0],
            'value': cookie[1]
        })

url = "https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=en-us"
driver.get(url)

cookies = open('/cookie.txt', 'r').read().strip()
set_cookies(driver, cookies)

driver.get(url)
time.sleep(5)

daily_count_xpath = "//body[1]/div[1]/div[2]/div[1]/div[3]/p[1]/span[1]"
daily_count = int(driver.find_element_by_xpath(daily_count_xpath).text)

reward_xpath = "//body/div[1]/div[2]/div[1]/div[4]/div[{}]".format(daily_count + 1)
driver.find_element_by_xpath(reward_xpath).click()
time.sleep(5)

driver.close()

report = open('/report.txt', 'a+')
report.write("Script executed at {}\n".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
report.close()