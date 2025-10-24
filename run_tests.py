import pytest
import tests

# Lista de archivos de pruebas a ejecutar
test_files = [
    "tests/test_inventory.py"
    #"tests/test_titulo.py"
    #"tests/test_login.py"
]

# Argumentos para ejecutar las pruebas  
pytest_args = test_files + ["--html=report_pepito.html"]

pytest.main(pytest_args)