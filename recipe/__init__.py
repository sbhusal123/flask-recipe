# Application Initializer

import os
import pathlib

from flask import Flask
from flask_orator import Orator


# ROOT directory
ROOT_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Get config file
config = os.environ['CONFIG']
config_file = os.getcwd() + config

"""Setup and config Flask app from config file"""
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile(config_file)

# Setup Static and Upload Path
UPLOAD_PATH = ROOT_DIR + app.config['UPLOAD_FOLDER']
app.config['UPLOAD_FOLDER'] = UPLOAD_PATH
if not pathlib.Path(UPLOAD_PATH).exists():
    os.makedirs(UPLOAD_PATH)

# Configue Orator
db = Orator(app)

def register_blueprints(application):
    from recipe.controllers import recipe
    application.register_blueprint(recipe)

def register_apis(application):
    prefix = '/api/v1.0'
    from recipe.api import recipe_api, auth_api
    app.register_blueprint(recipe_api, url_prefix=prefix)
    app.register_blueprint(auth_api, url_prefix=prefix)

register_apis(app)
register_blueprints(app)