"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }


    return jsonify(response_body), 200


@app.route('/members', methods=['POST'])
def add_member():

    # this is how you can use the Family datastructure by calling its methods
    response_body = request.json
    edad= response_body["age"]
    numeros_suerte= response_body["lucky_numbers"]
    name= response_body["name"]

    jackson_family.add_member(name, edad, numeros_suerte)


    return jsonify(response_body), 200



@app.route('/members/<int:member_id>', methods=['GET'])
def get_one_member(member_id):

    # this is how you can use the Family datastructure by calling its methods
    member = jackson_family.get_member(member_id)
    response_body = {
        "family": member
    }


    return jsonify(response_body), 200




@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_one_member(member_id):

    # this is how you can use the Family datastructure by calling its methods
    jackson_family.delete_member(member_id)
    members = jackson_family.get_all_members()


    return jsonify(members), 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
