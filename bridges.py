"""

PUENTES DE CONSUMO DE MAPON V1

"""
import requests
from datetime import date, timedelta
from config import MAPON_BASE_URL, MAPON_API_KEY



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



# LISTA DE UNIDAD "unit/list.json"
def unit_general_info(base_url=MAPON_BASE_URL, key=MAPON_API_KEY, unit_id=None):
    # CONSTRUIR ENDPOINT
    end_point = f"{base_url}unit/list.json?key={key}&unit_id={unit_id}"
    # EJECUTAR LA PETICION Y ALMACENAR 
    response = requests.get(end_point)

    if response.status_code==200:
        # CONVERTIR LA RESPUESTA EN JSON
        unit = response.json()["data"]["units"][0]
        return unit