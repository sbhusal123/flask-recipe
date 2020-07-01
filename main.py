# Starting Point of our application

from app import create_app
import os

config_file = os.getcwd() + "/config/development.cfg"
application = create_app(config_file)

"""Routes can also be defined here, but it's antipattern"""
@application.route('/')
def index():
    return "Hello world"

if __name__ == '__main__':
    application.run(host="localhost", port=8000, debug=True, use_reloader=True)