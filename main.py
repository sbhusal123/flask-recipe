# Starting Point of our application

from recipe import app
import os

"""Routes can also be defined here, but it's antipattern rather use blueprint"""
# @app.route('/')
# def index():
#     return "Hello world"

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True, use_reloader=True)