from flask import Flask
from importlib import import_module


def create_app():
    app = Flask(__name__, static_folder='base/static')  
   # register_blueprints(app)
    app.register_blueprint(import_module('app.{}.routes'.format('base')).blueprint)
    return app