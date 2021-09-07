import os
from flask import Flask 
from flask_bootstrap import Bootstrap
from .config import DevConfig

# template_dir = os.path.abspath('../frontend/')
# app = Flask(__name__, template_folder=template_dir)

app = Flask(__name__, instance_relative_config= True)

bootstrap = Bootstrap(app)

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views



