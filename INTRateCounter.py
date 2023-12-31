from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Download ChromeDriver from:
# https://sites.google.com/chromium.org/driver/

# Already installed ChromeDriver in our system path, so use the following command:
driver = webdriver.Chrome()
# Detail links: 
# https://stackoverflow.com/questions/42478591/python-selenium-chrome-webdriver
# https://www.swtestacademy.com/install-chrome-driver-on-mac/

driver.get("https://www.google.com")
