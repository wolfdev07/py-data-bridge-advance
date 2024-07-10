"""

PUENTES DE CONSUMO DE MAPON V1

"""
import requests
import json
import asyncio
import httpx
from datetime import date, timedelta
from config import MAPON_BASE_URL, MAPON_API_KEY, CRM_LOGIN_URL, COOKIES_SESSION_CRM
from config import save_crm_cookies
from bs4 import BeautifulSoup
from utils import login_crm



# LISTAR GRUPOS EMPRESARIALES.
def get_groups(base_url=MAPON_BASE_URL, key=MAPON_API_KEY, unit_id=None):
    # CONSTRUYE EL ENDPOINT
    end_point = f"{base_url}unit_groups/list.json?key={key}" 
    # SI CONTIENE PARAMETROS DE ID, LOS AGREGA.
    if unit_id is not None: 
        end_point = end_point + f"&unit_id={unit_id}"
    # EJECUTA LA PETICION, Y ALMACENA LA RESPUESTA EN LA VAR RESPONSE
    response = requests.get(end_point)

    # VERIFICA EL ESTADO DE LA RESPUESTA.
    if response.status_code == 200:
        # CONVIERTE LA RESPUESTA A JSON
        data = response.json()["data"]
        return data
    
    else:
        print("Error:", response.status_code)
        return None


# LISTAR UNIDADES POR GRUPO
def get_units_by_group(base_url=MAPON_BASE_URL, key=MAPON_API_KEY, group_id=None):
    # CONSTRUIR ENDPOINT
    end_point = f"{base_url}unit_groups/list_units.json?key={key}&id={group_id}"
    # EJECUTA LA PETICION Y ALMACENA LA RESPUESTA
    response = requests.get(end_point)

    print(response)

    # VERIFICA ESTADO DE LA RESPUESTA
    if response.status_code==200:
        #CONVERTIR LA RESPUESTA EN JSON
        data = response.json()
        print(data)
        return data
    else:
        print("Error:", response.status_code)
        return None


# REPORTE DE COMPORTAMIENTO(BEHAVIOUR) UNIDADES
def units_behaviour_report(base_url=MAPON_BASE_URL, key=MAPON_API_KEY, date_from=None, date_till=None, group_id=None):
    # VALIDA LAS FECHAS EN CASO DE DEJAR EN NONE, ASIGNA LOS ULTIMOS 30 DÍAS
    if date_till is None and date_from is None:
        date_till = date.today()
        date_from = date_till + timedelta(days=-29)

    # CONSTRUIR ENDPOINT
    end_point = f"{base_url}driver_behaviour/report_units.json?key={key}&date_from={date_from}&date_till={date_till}&group_id={group_id}"
    # EJECUTA LA PETICION Y ALMACENA LA RESPUESTA
    response = requests.get(end_point)

    if response.status_code==200:
        # CONVERTIR LA RESPUESTA EN JSON
        data = response.json()["data"] # DE RESPONSE SOLO SE NECESITA LA LIST DE ARRAYS

        # REGRESAR CONTEXTO
        context = { "data": data,
                    "date_from": date_from,
                    "date_till": date_till,
                    "group_id": group_id}
        
        return context
    else:
        print("Error:", response.status_code)
        return None


async def get_table_quicklink(url_target):
    # INICIAR SESIÓN
    async with httpx.AsyncClient() as session:
        # LOGIN SI NO HAY EN ENV, SETEAR LAS COOKIES
        if not COOKIES_SESSION_CRM:
            get_cookies = login_crm(CRM_LOGIN_URL)
            save_crm_cookies(get_cookies)
            cookies = get_cookies
        else:
            # CARGAR LAS COOKIES
            cookies = json.loads(COOKIES_SESSION_CRM)
            
        # SETEAR LAS COOKIES EN LA SESIÓN
        for cookie in cookies:
            session.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])
        
        try:
            # REALIZAR LA PETICIÓN Y ALMACENAR EL RESULTADO
            response = await session.get(url_target)
            
            # VERIFICAR SI LA SOLICITUD FUE EXITOSA
            if response.status_code == 200:
                # OBTENER EL CONTENIDO HTML
                doc_html = BeautifulSoup(response.content, 'html.parser')
                
                # ESPERAR HASTA QUE EXISTA LA ETIQUETA <table>
                await asyncio.wait_for(wait_for_table(doc_html), timeout=120)
                
                # PROCESAR LA TABLA
                target_tag = doc_html.find('table')
                if target_tag:
                    for tag in target_tag.find_all('tr'):
                        print(tag.text)
                else:
                    print("No se encontró la etiqueta <table> en el contenido HTML")
                
                return response.content
            else:
                print(f"Error: {response.status_code} - {response.reason}")
                return None
        except asyncio.TimeoutError:
            print("Tiempo de espera agotado al esperar la etiqueta <table>")
            return None
        except Exception as e:
            print(f"Error durante la solicitud HTTP: {e}")
            return None

# ESPERAR HASTA QUE EXISTA LA ETIQUETA <table>
async def wait_for_table(doc_html):
    while not doc_html.find('table'):
        await asyncio.sleep(1)

# EJECUTAR FUNCIONES
async def scrap_crm_async(url_target):
    await get_table_quicklink(url_target)

asyncio.run(scrap_crm_async("https://mapon.com/partner/incoming_data/?box_model=QUECLINK&unique_id=862524060583388"))
#scrap_crm("https://mapon.com/partner/incoming_data/?box_model=QUECLINK&unique_id=862524060583388")
# EJEMPLOS DE USO
#units_behaviour_report(base_url=MAPON_BASE_URL, key=MAPON_API_KEY, group_id=69153)