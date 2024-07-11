from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def login_crm(url_target):
    # CONFIGURAR EL NAVEGADOR
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # ABRIR LA PAGINA DE INICIO DE SESIÓN
    driver.get(url_target)
    # INGRESAR CREDENCIALES
    try:
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, "mp-dropdown-header")))
    except:
        print("Error al cargar la página")
    cookies = driver.get_cookies()
    # CERRAR EL NAVEGADOR
    driver.quit()
    return cookies