from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_cart(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    badge = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    assert badge.text == "1"


def test_remove_from_cart(logged_in_driver):
    driver = logged_in_driver

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    assert len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0