import backend.got_mongo as got_mongo

client = got_mongo.get_client()

def t_mongo():
    c = client
    print(list(c.list_databases()))

user_schema = {
    'userId': {
        'type': 'int',
        'required': True,
    },
    'firstName': {
        'type': 'string',
        'minlength': 1,
        'required': True,
    },
    'lastName': {
        'type': 'string',
        'minlength': 1,
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


t_mongo()