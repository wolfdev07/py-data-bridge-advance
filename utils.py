import os
import datetime
from selenium_functions import login_crm
from config import CRM_LOGIN_URL

now = datetime.datetime.now()

def process_string_util(string):
    process_string = string.replace("_", " ")
    process_string = process_string.upper()
    return process_string


def expiration_cookies(data_base, Model):
    try:
        cookies = data_base.session.get(Model, 1)
    except Exception as e:
        print(e)
        cookies = None
    if cookies is not None and now - cookies.updated_at < datetime.timedelta(hours=3):
        return cookies, f"LAS GALLETAS SIRVEN!!!: {cookies.updated_at} *******************", True
    elif cookies is not None and now - cookies.updated_at > datetime.timedelta(hours=3):
        return cookies, "HAY GALLETAS PERO YA NO SIRVEN, IR POR MÁS", False
    elif cookies is None:
        return cookies, "LAS GALLETAS NO EXISTEN", None


def cookies_manager(data_base, Model):

    cookies_exist, cookies_string, bool_cookies = expiration_cookies(data_base, Model)

    # HAY GALLETAS Y TODAVIA SIRVEN
    if cookies_exist is not None and now - cookies_exist.updated_at < datetime.timedelta(hours=3):
        print(cookies_string)
        cookies = cookies_exist

    # HAY GALLETAS PERO YA NO SIRVEN, IR POR MÁS
    elif cookies_exist is not None and now - cookies_exist.updated_at > datetime.timedelta(hours=3):
        print(cookies_string)
        
        cookies_list = login_crm(CRM_LOGIN_URL)[0]
        cookies_exist.domain = cookies_list["domain"]
        cookies_exist.http_only = cookies_list["httpOnly"]
        cookies_exist.name = cookies_list["name"]
        cookies_exist.path = cookies_list["path"]
        cookies_exist.same_site = cookies_list["sameSite"]
        cookies_exist.secure = cookies_list["secure"]
        cookies_exist.value = cookies_list["value"]
        cookies_exist.updated_at = now
        data_base.session.commit()
        cookies = data_base.session.get(Model, 1)
        print(f"SE ACTUALIZARON LAS GALLETAS CON EXITO: {cookies_exist.updated_at}")

    # NO HAY NI MADRES DE GALLETAS
    elif cookies_exist is None:
        print(cookies_string)
        cookies_list=login_crm(CRM_LOGIN_URL)[0]
        print(cookies_list)
        cookies = Model(
                        id=1, 
                        domain=cookies_list["domain"], 
                        http_only=cookies_list["httpOnly"], 
                        name=cookies_list["name"], 
                        path=cookies_list["path"], 
                        same_site=cookies_list["sameSite"], 
                        secure=cookies_list["secure"], 
                        value=cookies_list["value"],
                        updated_at=datetime.datetime.now()
                        )
        data_base.session.add(cookies)
        data_base.session.commit()

    return cookies


def cookies_converter(cookies_db):

    # CONVERTIR EN DICT
    cookies = {}
    cookies["domain"] = cookies_db.domain
    cookies["httpOnly"] = cookies_db.http_only
    cookies["name"] = cookies_db.name
    cookies["path"] = cookies_db.path
    cookies["sameSite"] = cookies_db.same_site
    cookies["secure"] = cookies_db.secure
    cookies["value"] = cookies_db.value

    return [cookies]



def html_table_constructor(table_element):
    # Convertir el elemento BeautifulSoup a una cadena HTML
    table_html = str(table_element)
    # Definir la ruta
    template_path = os.path.join('templates', 'pages', 'crm-manager', 'components', 'table.html')
    # Guardar la tabla en un archivo HTML
    with open(template_path, 'w', encoding='utf-8') as file:
        file.write(table_html)