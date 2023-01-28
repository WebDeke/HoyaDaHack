
from http.client import NOT_FOUND, responses
from . import db
from flask import Flask, request, jsonify
import backend.got_mongo as got_mongo
import jsonify
from pymongo import PyMongo
from bson.objectid import ObjectId


client = got_mongo.get_client()
collection = client['Users']
mongo = PyMongo(app)

def t_mongo():
    app = Flask(__name__)
    c = client
    print(list(c.list_databases()))

user_schema = {
    'userId': {
        'type': 'int',
        'unique': True,
        'required': True,
    },
    'firstName': {
        'type': 'string',
        'minlength': 1,
        'unique': True,
        'required': True,
    },
    'lastName': {
        'type': 'string',
        'minlength': 1,
        'unique': True,
        'required': True,
    },
    'courses': {
        'type': 'array',
        "required": False,
    },
    'studySpace':{
        'type':'string',
        'minlength':1,
        'required': True,
    },
    'phoneNo': {
        'type': 'int',
        'required': True,
    }
}

def create_user():
    """
       Function to create new users.
       """
    try:
        # Create new users
        try:
            values = request.get_json()
            fname = values.get("fname")
            lname = values.get("lname")
            collection.insert_one({"fname: ":fname, "lname":lname, "courses": None, "studySpace": None, "phoneNumber": None})
            
        except:
            # Bad request as request body is not available
            # Add message for debugging purpose
            return "", 400

    except:
        # Error while trying to create the resource
        # Add message for debugging purpose
        return "", 500


def get_users():
    users = client.db.collection.find()
    response = jsonify(users)
    return response


def add_classes(_id):
    if(_id):
        courses = request.json['classes']
        client.db.collection.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {"courses": courses})
        response = jsonify({'message': 'User' + _id + 'Updated Successfuly'})
        response.status_code = 200
        return response
    else:
        return NOT_FOUND()

def add_studySpace(_id):
    if(_id):
        space = request.json['space']
        client.db.collection.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {"studySpace": space})
        response = jsonify({'message': 'User' + _id + 'Updated Successfuly'})
        response.status_code = 200
        return response
    else:
        return NOT_FOUND()

def add_phone(_id):
    if(_id):
        phone = request.json['phone']
        client.db.collection.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {"phone": phone})
        response = jsonify({'message': 'User' + _id + 'Updated Successfuly'})
        response.status_code = 200
        return response
    else:
        return NOT_FOUND()


if __name__ == "__main__":
    app.run(debug=True, port=3000)

t_mongo()