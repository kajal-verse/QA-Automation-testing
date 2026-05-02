import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    # CI safe settings
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # IMPORTANT: no ChromeDriverManager here
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()