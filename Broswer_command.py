from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()

# Open URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)

# Maximize window
driver.maximize_window()
time.sleep(2)

# Confirm login container is present
try:
    driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-container")
    print("Login container found.")
except:
    print("Login container not found.")

time.sleep(2)

# Click on 'Forgot your password?' using correct CSS selector
try:
    forgot_button = driver.find_element(By.CSS_SELECTOR, "p.oxd-text.oxd-text--p.orangehrm-login-forgot-header")
    forgot_button.click()
    print("Clicked 'Forgot your password?'")
except Exception as e:
    print("Could not click on forgot password link:", e)

time.sleep(3)

# Navigate back to login page
driver.back()
print("Navigated back to login page")
time.sleep(3)

# Forward again (optional)
driver.forward()
print("Forward to Forgot Password page again")
time.sleep(2)

# Refresh the page
driver.refresh()
print("Page refreshed")
time.sleep(2)

# Navigate back to login page
driver.back()
print("Navigated back to login page")
time.sleep(3)

# Close the browser
driver.close()
