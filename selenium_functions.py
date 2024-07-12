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
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, "data_table")))
    table_element = driver.find_element_by_class_name("data_table")
    # Get the table caption (if it exists)
    caption_element = table_element.find_element(By.TAG_NAME, "caption")
    if caption_element:
        caption_text = caption_element.text
    else:
        caption_text = ""
    # Extract the table data
    table_data = []
    for row in table_element.find_elements(By.TAG_NAME, "tr"):
        row_data = []
        for cell in row.find_elements(By.TAG_NAME, "td"):
            row_data.append(cell.text)
        table_data.append(row_data)
    # Cerrar el controlador
    driver.quit()
    return table_data, caption_text