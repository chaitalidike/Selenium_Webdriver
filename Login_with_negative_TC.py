from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def open_browser():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    return driver

def test_positive_login():
    driver = open_browser()
    try:
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        logout_button = driver.find_element(By.XPATH, "//a[text()='Log out']")
        assert logout_button.is_displayed()
        print("Test Case: Positive Login - PASSED")
    except Exception as e:
        print("Test Case: Positive Login - FAILED:", e)
    finally:
        driver.quit()

def test_invalid_username():
    driver = open_browser()
    try:
        driver.find_element(By.ID, "username").send_keys("wronguser")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        error = driver.find_element(By.ID, "error").text
        assert "Your username is invalid!" in error
        print("Test Case: Invalid Username - PASSED")
    except Exception as e:
        print("Test Case: Invalid Username - FAILED:", e)
    finally:
        driver.quit()

def test_invalid_password():
    driver = open_browser()
    try:
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("WrongPassword")
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        error = driver.find_element(By.ID, "error").text
        assert "Your password is invalid!" in error
        print("Test Case: Invalid Password - PASSED")
    except Exception as e:
        print("Test Case: Invalid Password - FAILED:", e)
    finally:
        driver.quit()

def test_empty_credentials():
    driver = open_browser()
    try:
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        error = driver.find_element(By.ID, "error").text
        assert "Your username is invalid!" in error
        print("Test Case: Empty Credentials - PASSED")
    except Exception as e:
        print("Test Case: Empty Credentials - FAILED:", e)
    finally:
        driver.quit()

# Run all test cases
test_positive_login()
test_invalid_username()
test_invalid_password()
test_empty_credentials()
