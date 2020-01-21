# 模擬login登入
使用PYTHON搭配SELENIUM

1.先安裝python3的版本
https://www.python.org/downloads/windows/

2.下載chromeDriver(與系統對應的版本)
https://sites.google.com/a/chromium.org/chromedriver/home

3.開始寫CODE模擬

import time
from selenium import webdriver

#setting path
chrome_path = "chromedriver.exe"
web = webdriver.Chrome(chrome_path)
url=  "https://github.com/login"

#open browser to url address
web.get(url) 
time.sleep(3)

#input username
web.find_element_by_id('login_field').send_keys('tobasidemo')

#input password
web.find_element_by_id('password').send_keys('Tobasidemo1788')

#comit to login
web.find_element_by_name('commit').click()
time.sleep(5)

#close browser
web.close()
