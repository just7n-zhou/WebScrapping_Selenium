from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Download ChromeDriver from:
# https://sites.google.com/chromium.org/driver/


driver = webdriver.Chrome()
# Automate cookie clicker game
# Click on cookies to get points and use points to buy upgrades
driver.get("https://orteil.dashnet.org/cookieclicker/")

# The name of the element that we want to click on is "bigCookie"
cookie_id = "bigCookie"
cookiesNUM_id = "cookies"
# Before we can click on the cookie, the website will ask us to select a language 

upgrades_price_prefix = "productPrice"
upgrades_prefix = "product"

# Use XPATH syntax to search for specific text or attribute in the HTML
# Use //* and function contains to search for a text or attribute
# Here we searched for a text that contains "English"
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

# Find the language element and click on it
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

# Wait for the cookie element to be present
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

# After cookie element is present, we can click on it
cookie = driver.find_element(By.ID, cookie_id)

while True:
    # Click the cookie
    cookie.click()
    # Find the number of cookies shown on the website and convert it to a string with ".text"
    cookies_count = driver.find_element(By.ID, cookiesNUM_id).text.split(" ")[0]
    # Replace all the commas in the string with nothing, and convert it to an integer
    cookies_count = int(cookies_count.replace(",", ""))
    
    # There are 4 upgrades in the game
    for i in range(4):
        product_price = driver.find_element(By.ID, upgrades_price_prefix + str(i)).text.replace(",", "")

        # If the product price is not a number, skip it
        if not product_price.isdigit():
            continue

        product_price = int(product_price)
    
        # If we have enough cookies to buy the upgrade, buy it
        if cookies_count >= product_price:
            # Find the upgrade element and click on it
            product = driver.find_element(By.ID, upgrades_prefix + str(i))
            product.click()
            break