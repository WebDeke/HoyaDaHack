import sys
import pymongo
import config


def get_client():
    client = pymongo.MongoClient(
       config.mongodb_url
    )
    db = client.test
    return client


def t1():

    c = get_client()
    print(list(c.list_databases()))


if __name__ == "__main__":
    t1()
