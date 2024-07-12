from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


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

# SETTEAR LAS COOKIES EN CHROME
def auth_crm(url_target, cookies):
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url_target)
    # Eliminar todas las cookies
    driver.delete_all_cookies()
    # Añadir las cookies
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get(url_target)
    return driver

# EXTRAER LA INFORMACION DE LA TABLA
def get_data_table_crm(url_target, cookies):
    driver = auth_crm(url_target, cookies)
    try:
        # Esperar a que la tabla esté presente
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, "data_table")))
        # Esperar a que la tabla tenga al menos un par de filas (indicativo de que los datos están cargados)
        WebDriverWait(driver, 120).until(lambda d: len(d.find_elements(By.CSS_SELECTOR, ".data_table tr")) > 1)
        # Esperar un poco más para asegurar que los datos están completamente cargados (ajusta según sea necesario)
        WebDriverWait(driver, 10)
        # Obtener el HTML de la página
        doc_html = driver.page_source
    finally:
        # Cerrar el controlador
        driver.quit()
    # Analizar el HTML con BeautifulSoup
    soup = BeautifulSoup(doc_html, "html.parser")
    table_element = soup.find("table", {"class": "data_table"})
    return table_element