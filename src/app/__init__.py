""" App entry point. """
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

def create_app():
    """ Function for bootstrapping Flask app. """
    application = Flask(__name__)
    application.config['CORS_HEADERS'] = ['Content-Type']
    CORS(application, supports_credentials=True, origins=['http://localhost:3000'])

    api = Api(application)