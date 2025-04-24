from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome browser
browser = webdriver.Chrome()

# Open the OrangeHRM login page
browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print('Open Browser')

# Print the page title
title = browser.title
print(title)

#  Correct way to minimize window
browser.minimize_window()

# Wait for the page to load completely
time.sleep(5)

#  Optional: Enter username (uncomment if needed)
username = browser.find_element(By.NAME, "username")
username.send_keys("Admin")

# Hold browser open for demo purposes
time.sleep(200)

# Optional: browser.quit()
