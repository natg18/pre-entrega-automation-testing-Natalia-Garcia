
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_inventory(login_in_driver): 

    try: 
        driver = login_in_driver

    except Exception as e: 
        print (f"Error en test_inventory: {e}")
        raise
    finally:
        driver.quit()