# project/server/__init__.py

import os

from flask import Flask,Blueprint
from customer.cust_api import ns as customerapi
from api.restplus import api
from db_conn import db

def initialize(my_app):
    blueprint = Blueprint('api', __name__, url_prefix='/api')

    api.init_app(blueprint)
    api.add_namespace(customerapi)
    my_app.register_blueprint(blueprint)
    db.init_app(app)
    
    print('After Initialize')
    
app = Flask(__name__)
initialize(app)
app.config.from_object('settings')

@app.route('/')
def index():
    return 'Welcome to renting cars'

if __name__ == "__main__":
    app.run()