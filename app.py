import webview
from flask import Flask, request, render_template
from bridges import get_groups, units_behaviour_report
from utils import processString


app = Flask(__name__)
window = webview.create_window('Data Bridge Advance', app)

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


@app.route('/hello-world')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
    #webview.start()