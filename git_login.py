
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


