from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_logout(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    logout_link = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
    logout_link.click()
    wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
    assert "saucedemo.com" in driver.current_url
    print(" Test Passed: Logout")
    time.sleep(2)