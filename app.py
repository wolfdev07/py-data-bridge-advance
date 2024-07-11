from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def run_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databridges.db'
    db.init_app(app)

    # IMPORTAR RUTAS
    from routes import register_routes
    register_routes(app, db)
    migrate = Migrate(app, db)
    return app

def init_db():
    app = run_app()
    with app.app_context():
        db.create_all()