import webview
from app import run_app, init_db


app = run_app()
window = webview.create_window('Data Bridge Advance', app)


if __name__ == '__main__':
    app.run(debug=True)
    init_db()
    #webview.start()