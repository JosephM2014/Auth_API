# Local Imports.
from instance.config import APP_CONFIG
from .database import create_tables

# Standard Library Imports.
from datetime import timedelta

# Third Party Imports.
from flask import Flask
from flask_jwt_extended import JWTManager

def create_app(config_name=None):
    app = Flask(__name__)
    create_tables()
    app.url_map.strict_slashes = False
    
    # Configurations.
    app.config.from_object(APP_CONFIG[config_name])
    app.config.from_pyfile('../instance/config.py')

    # JWT Configurations.
    manager = JWTManager(app=app)

    #Local Configurations.
    from .api.v2 import version2, api
    app.register_blueprint(version2)
    manager._set_error_handler_callbacks(api)

    return app
