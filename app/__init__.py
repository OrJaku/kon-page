from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()


def create_app(app_config):
    app = Flask(__name__, template_folder='templates')
    db.init_app(app)
    app.config.from_object(app_config)
    from .main_app import views
    app.register_blueprint(views.main)
    from .advert_app import views
    app.register_blueprint(views.advert)
    return app
