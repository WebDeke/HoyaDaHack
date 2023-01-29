
from http.client import NOT_FOUND, responses
from . import db
from flask import Flask, request, jsonify
import backend.got_mongo as got_mongo
import jsonify
from pymongo import PyMongo
from bson.objectid import ObjectId


client = got_mongo.get_client()
collection = client['Users']
mongo = PyMongo()

def t_mongo():
    app = Flask(__name__)
    c = client
    print(list(c.list_databases()))

user_schema = {
    'id': {
        'type': 'int',
        'unique': True,
        'required': True,
    },
    'fname': {
        'type': 'string',
        'minlength': 1,
        'unique': True,
        'required': True,
    },
    'lname': {
        'type': 'string',
        'minlength': 1,
        'unique': True,
        'required': True,
    },
    'courses': {
        'type': 'array',
        "required": False,
    },
    'space':{
        'type':'string',
        'minlength':1,
        'required': True,
    },
    'phone': {
        'type': 'int',
        'required': True,
    }
}

def get_users():
    users = client.db.collection.find()
    response = jsonify(users)
    return response

def create_user(_id, record):
    client.db.collection.insert_one(record)
    response = jsonify({'message': 'User' + _id + 'Updated Successfuly'})
    response.status_code = 200
    return response


def listFirstNames():
   
    return collection.distinct('fname')
def listLastNames():
    return collection.distinct('lname')

# def checkIfDuplicate(fname, lname):
#     firstNames = listFirstNames()
#     lastNames = listLastNames()
#     for i in range(0, len(firstNames)):
#         for j in range(0, len(lastNames)):
#             if(fname == firstNames[i] and lname == lastNames[j]):
#                 return True
#     return False


# def add_classes(_id):
#     if(_id):
#         courses = request.json['classes']
#         client.db.collection.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {"courses": courses})
#         response = jsonify({'message': 'User' + _id + 'Updated Successfuly'})
#         response.status_code = 200
#         return response
#     else:
#         return NOT_FOUND()
# def add_studySpace(_id):
#     if(_id):
#         space = request.json['space']
#         client.db.collection.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {"studySpace": space})
#         response = jsonify({'message': 'User' + _id + 'Updated Successfuly'})
#         response.status_code = 200
#         return response
#     else:
#         return NOT_FOUND()

# def add_phone(_id):
#     if(_id):
#         phone = request.json['phone']
#         client.db.collection.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {"phone": phone})
#         response = jsonify({'message': 'User' + _id + 'Updated Successfuly'})
#         response.status_code = 200
#         return response
#     else:
#         return NOT_FOUND()


if __name__ == "__main__":
    app.run(debug=True, port=3000)

t_mongo()