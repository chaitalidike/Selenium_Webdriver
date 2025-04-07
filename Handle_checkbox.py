from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Open a practice form with checkboxes
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()
time.sleep(2)

#  Locate checkbox (Example: ID = 'hobbies')
checkbox = driver.find_element(By.ID, "hobbies")

#  Check if the checkbox is selected
if not checkbox.is_selected():
    checkbox.click()
    print("Checkbox is now selected.")
else:
    print("Checkbox was already selected.")

time.sleep(2)

#  Uncheck the checkbox
if checkbox.is_selected():
    checkbox.click()
    print("Checkbox is now unselected.")
else:
    print("Checkbox was already unselected.")

time.sleep(2)

#  Close the browser
driver.quit()
