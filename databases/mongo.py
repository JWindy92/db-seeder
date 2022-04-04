# Connect to mongodb
from pymongo import MongoClient

class MongoConnection extends DbConnection:

    def __init__(self, config):
        print(f"Connection to MongoDB")
        client = MongoClient(config["host"], config["port"])

    def template_func(self):
        print("calling from mongo")