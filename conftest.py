import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="function")
def driver():
    firefox_options = Options()
    firefox_options.set_preference("browser.privatebrowsing.autostart", True)
    firefox_options.add_argument("--width=1600")
    firefox_options.add_argument("--height=900")
    driver = webdriver.Firefox(options=firefox_options)
    yield driver
    driver.quit()
