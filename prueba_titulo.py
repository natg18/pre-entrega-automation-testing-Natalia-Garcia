from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

try:
    driver.get("https://www.saucedemo.com/")
    print("Titulo:", driver.title)
    assert driver.title == "Swag Labs"
    time.sleep(2)
finally: 
    driver.quit()