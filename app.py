from flask import Flask, request, render_template
from bridges import get_groups, units_behaviour_report

app = Flask(__name__)

# DASH DE INICIO
@app.route('/', methods=['GET'])
def index():
    # GRUPOS DE CLIENTES
    groups = get_groups()
    return render_template('pages/index/index.html', groups=groups)

# REPORTE DE UNIDADES POR GRUPO
@app.route('/units-report-group', methods=['GET', 'POST'])
def units_report_group():
    # SI EL METODO ES POST
    if request.method == 'POST':
        id_group = request.form.get('id_group')
        # EN CASO DE QUERER FECHAS ESPECIFICAS
        if request.form.get('data_till') and request.form.get('data_from'):
            data_till=request.form.get('data_till')
            data_from=request.form.get('data_from')
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