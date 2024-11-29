from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Ruta al WebDriver (asegurándote que la ruta esté bien formateada)
driver_path = "C:/Users/HP VICTUS/Downloads2/chromedriver.exe"  # Usa la barra normal o barra invertida doble

# Crea un objeto Service
service = Service(driver_path)

# Inicia el navegador con el objeto Service
driver = webdriver.Chrome(service=service)

try:
    # Accede a tu página local
    driver.get("http://127.0.0.1:8000/")
    
    # Espera unos segundos (si es necesario)
    time.sleep(2)

    # Interactúa con el login (ejemplo)
    username = driver.find_element(By.NAME, "administrador")
    password = driver.find_element(By.NAME, "administrador")
    login_button = driver.find_element(By.ID, "login-btn")

    # Ingresa credenciales
    username.send_keys("administrador")
    password.send_keys("administrador")
    login_button.click()
    
    # Espera a que cargue la siguiente página
    time.sleep(3)
    
    # Verifica si el login fue exitoso (por ejemplo, buscando un elemento específico)
    assert "Panel de citas" in driver.page_source

finally:
    # Cierra el navegador
    driver.quit()
