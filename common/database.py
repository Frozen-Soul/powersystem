

import pymongo


class Database(object):
    URI = "mongodb+srv://sharpnel:qwerty123@powersystem-chebt.mongodb.net/test?retryWrites=true"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['power']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def initializing_City(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def update(collection, query):
        return Database.DATABASE[collection].update_one(query)