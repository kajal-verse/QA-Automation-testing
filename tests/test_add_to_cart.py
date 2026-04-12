from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()
    cart_badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert cart_badge.text == "1"
    print("Test Passed: Add to Cart")

def test_remove_from_cart(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    driver.find_element(By.XPATH, "//button[text()='Remove']").click()
    badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(badges) == 0
    print("Test Passed: Remove from Cart")