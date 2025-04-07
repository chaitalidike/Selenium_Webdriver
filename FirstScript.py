from selenium.webdriver.common.by import By
import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print('Open Browser')
title = browser.title
print(title)
browser.minimize.window()
## username = browser.find.element
## username.send_keys('student')
time.sleep(200)
