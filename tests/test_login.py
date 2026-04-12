import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_valid_login(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url
    print("Test Passed: Valid Login")

def test_invalid_login(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrongpassword")
    driver.find_element(By.ID, "login-button").click()
    error = driver.find_element(By.CLASS_NAME, "error-message-container")
    assert error.is_displayed()
    print("Test Passed: Invalid Login Shows Error")

def test_locked_out_user(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    error = driver.find_element(By.CLASS_NAME, "error-message-container")
    assert error.is_displayed()
    print("Test Passed: Locked Out User Shows Error")