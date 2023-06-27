from flask import Blueprint, jsonify
from flask_cors import CORS

HelloWorld = Blueprint('Project', __name__)

CORS(Project,supports_credentials=True)

@HelloWorld.route('/', methods=['GET'])
def helloWorld():
    return jsonify({
        'msg': 'hello world'
    }),400