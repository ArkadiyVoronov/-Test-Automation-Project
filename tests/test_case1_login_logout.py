import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    # Set up the WebDriver instance
    driver = webdriver.Chrome()  # You need to have ChromeDriver installed and in PATH
    yield driver
    # Teardown - Quit the WebDriver instance
    driver.quit()


def test_login_logout(browser):
    # Go to the home page
    browser.get("https://practicetestautomation.com/practice-test-login/")
