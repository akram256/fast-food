"""
   Module for starting/ running the app
"""
from flask import Flask
from urls import Urls
APP = Flask(__name__)
APP.config.from_object('config.DevelopmentConfig')
Urls.fetch_urls(APP)
if __name__ == '__main__':
    APP.run()
    