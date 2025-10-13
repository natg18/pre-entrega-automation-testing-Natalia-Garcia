from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

try:
    # Login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    #Validación de la redirección de la página
    assert '/inventory.html' in driver.current_url

    # Existencia de menu
    menu = driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
    assert menu

    # Existencia de dropdown de filtro
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed()
    assert filtro

    # Interacciones
    productos = driver.find_elements(By.CLASS_NAME,"inventory_item")
    productos[0].find_element(By.TAG_NAME, "button").click()
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert carrito == "1"

    # Nombre y precio del primer producto
    assert productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text == "Sauce Labs Backpack"
    assert productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text == "$29.99"

    productos[0].find_element(By.ID, "item_4_title_link").click()

    #Validación de la redirección de la página
    assert '/cart.html' in driver.current_url
    
    #lista_carrito = driver.find_elements(By.CLASS_NAME,"cart_item")
    #lista_carrito[0]

    print("TEST OK")
    '''except Exception as e: 
    print ("Error en test: ", e)
    raise'''
finally:
    driver.quit()

