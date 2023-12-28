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

# Wait for presence of the element we want, here is 5 seconds
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

# Find the element by CLASS_NAME, here is the search box input element
input_element = driver.find_element(By.CLASS_NAME,"gLFyf")
# Clear any content in the search box 
input_element.clear()
# Send input to the search box element
input_element.send_keys("Tech with Tim" + Keys.ENTER)

# Once searched an element, we want to find a link with partial text "Tech With Tim"
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")

# If we want to find the exact text, we can use the following command:
# link = driver.find_element(By.LINK_TEXT, "Tech With Tim")

# If we want to find multiple elements containing a partial text, we can use the following command:
# links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Tech With Tim")
# This returns an array that we can iterate through and click the one we want

# Click the link and redirect to the link
link.click()

time.sleep(5)

driver.quit()
