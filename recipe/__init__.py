# Application Initializer

import os
from flask import Flask
from flask_orator import Orator
import os

# ROOT directory
ROOT_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Get config file
config_file = os.getcwd() + "/config/development.cfg"

# Setup and configure flask app from config file
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile(config_file)
app.config['UPLOAD_FOLDER'] = ROOT_DIR + app.config['UPLOAD_FOLDER']

# Configur Orator
db = Orator(app)


prefix = '/api/v1.0'

def register_blueprints(application):
    from recipe.controllers import recipe
    application.register_blueprint(recipe)

def register_apis(application):
    from recipe.api import recipe_api, auth_api
    app.register_blueprint(recipe_api, url_prefix=prefix)
    app.register_blueprint(auth_api, url_prefix=prefix)

register_apis(app)
register_blueprints(app)