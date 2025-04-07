import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Launch browser
driver = webdriver.Chrome()

# Open the page with the dropdown
url = "https://the-internet.herokuapp.com/dropdown"
driver.get(url)

# Wait for page load
time.sleep(3)

#  Locate the dropdown element
dropdown_element = driver.find_element(By.ID, "dropdown")

#  Create Select object
select = Select(dropdown_element)

#  Select by index (0-based; 1 means second option)
select.select_by_index(1)
time.sleep(2)

#  Select by value (value="2")
select.select_by_value("2")
time.sleep(2)

#  Select by visible text
select.select_by_visible_text("Option 1")
time.sleep(2)

#  Close browser
driver.quit()
