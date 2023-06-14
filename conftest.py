import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
s = Service(CHROMEDRIVER_PATH)
WINDOW_SIZE = "1920,1080"
# Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('--no-sandbox')
from time import sleep

if sys.platform == 'win32':
    driver = webdriver.Chrome(ChromeDriverManager().install())
if sys.platform == 'linux':
    driver = driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.maximize_window()
# Get the response and print title
driver.get("https://www.python.org")
print(driver.title)
driver.close()
