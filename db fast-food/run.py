"""
This module runs the application
"""

"""
This is the main module
"""
from flask import Flask
from routes.urls import Urls
from controllers.database_connection import Databaseconn
from flask_jwt_extended import JWTManager


db = Databaseconn()
db.create_tables()

APP = Flask(__name__)

APP.config['JWT_SECRET_KEY'] = 'codeislove' 
jwt = JWTManager(APP)

APP.env = 'development'
APP.testing = True

Urls.generate_url(APP)
if __name__ == '__main__':
    
    APP.run(debug = True)