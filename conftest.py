import pytest
from selenium import webdriver
from pages.login_page import LoginPage
import tempfile

@pytest.fixture
def driver(): 

    #1) Crear un perfil temporal (se borra al terminar tu script si lo eliminas)
    tmp_profile = tempfile.mkdtemp()

    options = webdriver.ChromeOptions()

    # Usar un perfil limpio para que no haya contraseñas guardadas
    options.add_argument(f"--user-data-dir={tmp_profile}")

    # 2) Desactivar el gestor de contraseñas y el popup de leak detection
    prefs = {
        "credentials_enable_service": False,       # no usar Google Password Manager
        "profile.password_manager_enabled": False  # no sugerir guardar contraseñas
    }
    options.add_experimental_option("prefs", prefs)

    # 3) Desactivar la feature de comprobación de contraseñas vulneradas
    options.add_argument("--disable-features=PasswordLeakDetection")

    # (Opcional) minimizar otras interrupciones típicas
    options.add_argument("--incognito")                 # sesión sin extensiones del perfil
    options.add_argument("--disable-notifications")     # notificaciones web
    options.add_argument("--disable-save-password-bubble")

    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver, usuario, password):
    LoginPage(driver).abrir_pagina().login_completo(usuario,password)
    return driver
