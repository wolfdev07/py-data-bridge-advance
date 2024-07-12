import datetime
from selenium_functions import login_crm
from config import CRM_LOGIN_URL


cookies = {"domain": "mapon.com", "httpOnly": True, "name": "PHPSESSID", "path": "/", "sameSite": "Lax", "secure": True, "value": "bddef210e347b5c976db9a895edf894c"}

def process_string_util(string):
    process_string = string.replace("_", " ")
    process_string = process_string.upper()
    return process_string


def cookies_manager(db, Model):

    cookies_exist = db.get_or_404(Model, 1)
    now = datetime.datetime.now()

    # HAY GALLETAS Y TODAVIA SIRVEN
    if cookies_exist.updated_at and now - cookies_exist.updated_at < datetime.timedelta(hours=1):
        print(f"LAS GALLETAS EXITEN: {cookies_exist.updated_at} *******************")
        cookies = cookies_exist

    # HAY GALLETAS PERO YA NO SIRVEN, IR POR MÁS
    elif cookies_exist.updated_at and now - cookies_exist.updated_at > datetime.timedelta(hours=1):
        print("HAY GALLETAS PERO YA NO SIRVEN, IR POR MÁS")
        
        cookies_list = login_crm(CRM_LOGIN_URL)[0]
        cookies_exist.domain = cookies_list["domain"]
        cookies_exist.http_only = cookies_list["httpOnly"]
        cookies_exist.name = cookies_list["name"]
        cookies_exist.path = cookies_list["path"]
        cookies_exist.same_site = cookies_list["sameSite"]
        cookies_exist.secure = cookies_list["secure"]
        cookies_exist.value = cookies_list["value"]
        cookies_exist.updated_at = now
        db.session.commit()
        cookies = db.get_or_404(Model, 1)
        print(f"SE ACTUALIZARON LAS GALLETAS CON EXITO: {cookies_exist.updated_at}")

    # NO HAY NI MADRES DE GALLETAS
    elif not cookies_exist:
        print("LAS GALLETAS NO EXISTEN")
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
        db.session.add(cookies)
        db.session.commit()

    return cookies