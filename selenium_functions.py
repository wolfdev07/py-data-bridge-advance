import json
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


def get_data_table_crm(url_target, COOKIES_SESSION_CRM):
    # SETTEAR LAS COOKIES
    chrome_options = Options()
    cookies_data = json.loads(COOKIES_SESSION_CRM)
    for cookie in cookies_data:
        chrome_options.add_cookie(cookie)
    # INIT chrome web driver
    driver = webdriver.Chrome(options=chrome_options)
    # ABRIR LA PAGINA
    driver.get(url_target)