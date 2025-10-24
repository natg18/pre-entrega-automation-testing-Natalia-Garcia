from selenium.webdriver.common.by import By
import time
import tempfile
from selenium import webdriver

def login(driver): 
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)


def config_driver():
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

    driver = webdriver.Firefox()

    return driver