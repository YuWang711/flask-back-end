from flask import Flask, session, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import ( 
    JWTManager
)
import logging
import config as con
from flask_mail import Mail


logging.basicConfig(level=logging.DEBUG)

mail = Mail()
jwt = JWTManager()

class APIFlaskWrapper(object):
    app = Flask("Api")

    def __init__(self, name):
        self.addConfig()
        CORS(self.app, supports_credentials=True)
        jwt.init_app(self.app)
        mail.init_app(self.app)
     
    def addConfig(self):
        pass

    def addBlueprints(self, blueprint):
        self.app.register_blueprint(blueprint)
        
    def runTestClient(self):
        return self.app.test_client()

    def runServer(self):
        self.app.run()


