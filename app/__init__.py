import os
from flask import Flask 
from flask_bootstrap import Bootstrap
from flask_restful import Api

from .main import main as main_blueprint
from .request import configure_request
from .config import config_options
from .api.v1 import apiv1
from .jwt_instance import jwt
from .db_instance import db

# template_dir = os.path.abspath('../frontend/')
# app = Flask(__name__, template_folder=template_dir)

bootstrap = Bootstrap()


def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)
    jwt.init_app(app)

    # Initializing flask extensions
 
    app.register_blueprint(main_blueprint)
    app.register_blueprint(apiv1)

    db.init_app(app)
    configure_request(app)
   

    # Will add the views and forms

    return app


