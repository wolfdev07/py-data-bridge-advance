import webview
from flask import Flask, request, render_template
from bridges import get_groups, units_behaviour_report

app = Flask(__name__)
window = webview.create_window('Data Bridge Advance', app)

# DASH DE INICIO
@app.route('/', methods=['GET'])
def index():
    # GRUPOS DE CLIENTES
    groups = get_groups()
    len_groups = len(groups)
    # RENDERIZAR LA RESPUESTA
    return render_template('pages/index/index.html', groups=groups, len_groups=len_groups)

# REPORTE DE UNIDADES POR GRUPO
@app.route('/units-report-group', methods=['GET'])
def units_report_group():
    # SOLO POR GET
    id_group = request.args.get('id_group')
    print(format(id_group))
    # EN CASO DE QUERER FECHAS ESPECIFICAS
    if request.args.get('data_till') and request.args.get('data_from'):
        data_till=request.args.get('data_till')
        data_from=request.args.get('data_from')
        units_report=units_behaviour_report(group_id=id_group, data_till=data_till, data_from=data_from)
    else:
        units_report=units_behaviour_report(group_id=id_group)
        # RENDERIZAR LA RESPUESTA
    return render_template('pages/units-list-group/units-report-group.html', id_group=id_group, units_report=units_report)


@app.route('/hello-world')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
    #webview.start()