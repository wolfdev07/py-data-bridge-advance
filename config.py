import os
import json
from dotenv import load_dotenv


# CARGAR VARIABLES DE ENTORNO
load_dotenv()
MAPON_BASE_URL = os.getenv('MAPON_BASE_URL')
MAPON_API_KEY = os.getenv('MAPON_API_KEY')
CRM_LOGIN_URL = os.getenv('CRM_LOGIN_URL')
COOKIES_SESSION_CRM = os.getenv("COOKIES_SESSION_CRM")


# SALVAR LAS COOKIES EN DURO
def save_crm_cookies(cookies):
    cookies_json = json.dumps(cookies)
    with open('.env', 'a') as file:
        set_cookies = f"COOKIES_SESSION_CRM={cookies_json}\n"
        file.write(set_cookies)
    return set_cookies

