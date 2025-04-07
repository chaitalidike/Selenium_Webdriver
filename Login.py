from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Step 1: Navigate to the login page
url = "https://practicetestautomation.com/practice-test-login/"
driver.get(url)

# Step 2: Login with valid credentials
username_enter = "student"
password_enter = "Password123"

driver.find_element(By.ID, "username").send_keys(username_enter)
driver.find_element(By.ID, "password").send_keys(password_enter)
driver.find_element(By.ID, "submit").click()

# Step 3: Assert successful login by checking the presence of the logout button
time.sleep(2)  # Wait for the page to load
logout_button = driver.find_element(By.XPATH, "//a[text()='Log out']")
assert logout_button.is_displayed(), "Login failed - Logout button not found"

# Step 4: Click the logout button
logout_button.click()

# Step 5: Assert redirect to login page by checking for login form elements
time.sleep(2)  # Wait for redirect
assert "practice-test-login" in driver.current_url, "Logout failed - Did not return to login page"
assert driver.find_element(By.ID, "username").is_displayed(), "Login form not visible after logout"

print("Test Passed: Login and logout flow working as expected.")

# Close the browser
driver.quit()
