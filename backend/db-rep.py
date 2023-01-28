import backend.got_mongo as got_mongo

client = got_mongo.get_client()

def t_mongo():
    c = client
    print(list(c.list_databases()))


t_mongo()