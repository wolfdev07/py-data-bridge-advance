from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def login_crm(url_target):
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


def get_data_table_crm(url_target, cookies):
    # LISTAR
    cookies = [cookies]
    # Configurar las opciones de Chrome
    chrome_options = Options()
    # Iniciar el controlador de Chrome
    driver = webdriver.Chrome(options=chrome_options)
    
    # Abrir la página para establecer un contexto en el que las cookies puedan ser añadidas
    driver.get(url_target)
    # Eliminar todas las cookies
    driver.delete_all_cookies()

    # Añadir las cookies
    for cookie in cookies:
        driver.add_cookie(cookie)

    # Recargar la página para que las cookies se apliquen
    driver.get(url_target)
    
    # Aquí puedes agregar el código para extraer la información que necesitas
    # ...
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, "web_os")))
    
    # Cerrar el controlador
    driver.quit()