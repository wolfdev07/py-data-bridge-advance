from flask import render_template, request
from models import Cookies
from bridges import get_groups, units_behaviour_report, unit_general_info
from utils import processString


def register_routes(app, db):

    # DASH DE INICIO
    @app.route('/', methods=['GET'])
    def index():
        # GRUPOS DE CLIENTES
        groups = get_groups()
        # RENDERIZAR LA RESPUESTA
        return render_template('pages/index/index.html', groups=groups)

    # REPORTE DE UNIDADES POR GRUPO
    @app.route('/units-report-group', methods=['GET'])
    def units_report_group():
        # EXTRAER LOS ARGS GET
        id_group = request.args.get('id_group')
        name_group = request.args.get('name_group')
        name_group = processString(name_group)
        # EN CASO DE QUERER FECHAS ESPECIFICAS
        if request.args.get('data_till') and request.args.get('data_from'):
            data_till=request.args.get('data_till')
            data_from=request.args.get('data_from')
            report=units_behaviour_report(group_id=id_group, data_till=data_till, data_from=data_from)
        else:
            report=units_behaviour_report(group_id=id_group)
            # RENDERIZAR LA RESPUESTA
            units_report = report["data"]
            period = f"{report['date_from']} - {report['date_till']}"
        return render_template('pages/units-list-group/units-report-group.html', 
                                period=period, 
                                units_report=units_report, 
                                name_group=name_group )


    @app.route("/unit-general-info", methods=['GET'])
    def unit_general_info_view():
        # EXTRAER LOS ARGS GET
        unit_id = request.args.get("unit_id")
        unit_info = unit_general_info(unit_id=unit_id)
        print(unit_info)
        # RENDERIZAR LA RESPUESTA
        return render_template('pages/unit-general/unit_general.html', unit_info=unit_info)


    @app.route('/hello-world')
    def hello_world():
        return 'Hello, World!'