from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from utils.datos import leer_csv_login
from pages.login_page import LoginPage

@pytest.mark.parametrize("usuario, password, debe_funcionar", leer_csv_login("datos/data_login.csv"))
def test_login_validation(login_in_driver, usuario, password, debe_funcionar): 
    try: 
        driver = login_in_driver
        
        if debe_funcionar == True:
            assert "/inventory.html" in driver.current_url, "No se redirigió al inventario."
        else: 
            mensaje_error = LoginPage(driver).obtener_error()
            assert "Epic sadface" in mensaje_error, "El mensaje de error no se está mostrando"

    except Exception as e: 
        print(f"Error en test_login: {e}")
        raise
    finally: 
        driver.quit()