# Application Initializer

import os
from flask import Flask
from flask_orator import Orator
import os

# Get config file
config_file = os.getcwd() + "/config/development.cfg"

# Setup and configure flask app from config file
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile(config_file)

# Configur Orator
db = Orator(app)