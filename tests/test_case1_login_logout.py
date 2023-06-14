import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Create ChromeOptions object and configure headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# Initialize the ChromeDriver with the options
driver = webdriver.Chrome(options=chrome_options)

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
