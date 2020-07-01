# Application Initializer

import os
from flask import Flask
# from flask_orator import Orator

def create_app(config_fileame=None):
    """Return application instance with config"""
    # Crete application Instance
    application = Flask(__name__, instance_relative_config=True)
    # Configure application from external file
    application.config.from_pyfile(config_fileame)
    # Configure Database with Orator
    application.config['ORATOR_DATABASES'] = {
        'development': {
            'driver': 'postgres',
            'database': 'recipe'
        }
    }
    return application

# def initialize_extension(application):
#     """Initialize Orator ORM extension"""
#     db = Orator(application)