from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_logout(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, "react-burger-menu-btn").click()

    logout_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )

    logout_btn.click()

    assert "saucedemo" in driver.current_url