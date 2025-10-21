from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import pytest

def test_titulo():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)

    try:
        driver.get("https://www.saucedemo.com/")
        print("Titulo:", driver.title)
        assert driver.title == "Swag Labs", "El título es incorrecto"
        time.sleep(2)

        print("Test título: OK")
    except Exception as e: 
        print(f"Error en test_login: {e}")
        raise
    finally: 
        driver.quit()