from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config





db = SQLAlchemy()

def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .mpesa import mpesa_bp

    app.register_blueprint(mpesa_bp)

    db.init_app(app)


    return app