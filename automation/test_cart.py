from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)

    # Wait for product page
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # Click Add to Cart
    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()

    # Wait for badge element
    badge = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    # Strong assertion (BEST PRACTICE)
    assert badge.text == "1"