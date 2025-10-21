from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import tempfile

def test_inventory(): 
    # 1) Crear un perfil temporal (se borra al terminar tu script si lo eliminas)
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

    #driver = webdriver.Chrome(options=options)
    driver = webdriver.Firefox()

    #driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    try: 
        
        #Validar título de la página
        driver.get("https://www.saucedemo.com/")
        assert driver.title == "Swag Labs", "El título es incorrecto"

        print("Test título: OK")

        #Validar login y redirección correcta
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        time.sleep(2)
        
        assert '/inventory.html' in driver.current_url, "No se redirigió al inventario."

        print("Test Login: OK")

        #Validar existencia de menú y filtros
        menu = driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
        assert menu, "No se muestra el menú."
        print("El menú está visible")

        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed()
        assert filtro
        print("Los filtros están visibles")

        #Validar existencia de productos
        productos = driver.find_elements(By.CLASS_NAME,"inventory_item")
        assert len(productos) > 0, "No hay productos visibles en la página."
        print("Hay productos visibles en la página")

        #Validar nombre y precio del primer ítem de la lista
        nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        assert nombre == "Sauce Labs Backpack"
        precio = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text
        assert precio == "$29.99"
        print(f"Se muestran nombre y precio correctos: {nombre}, {precio}")

        #Validar agregar un ítem al carrito
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(2)
        carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert carrito == "1", "No se muestra la cantidad correcta de ítems en el carrito."
        print(f"El carrito muestra {carrito} item")

        #Validar redirección al carrito
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        assert '/cart.html' in driver.current_url, "No se redirigió correctamente al carrito"
        print("Se redirigió correctamente al carrito")

        #Validar que se muestre el ítem agregado en el listado del carrito
        items_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
        
        #Validar nombre del item
        item_nombre = items_carrito[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        assert item_nombre == "Sauce Labs Backpack"
        print(f"El nombre del item del carrito es correcto: {item_nombre}")

        #Validar precio del item
        item_precio = items_carrito[0].find_element(By.CLASS_NAME, "inventory_item_price").text
        assert item_precio == "$29.99", "El precio del item del carrito es incorrecto."
        print(f"El precio del item del carrito es correcto: {item_precio}")
    
    except Exception as e: 
        print ("Error en test: ", e)
        raise
    finally:
        driver.quit()