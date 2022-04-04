import databases.mongo
import databases.mysql

class DbConnection:

    def __init__(self,config):
        self.config = config
        if config["engine"] == "mongo":
            self.conn = databases.mongo.MongoConnection(config)
        elif config["engine"] == "mysql":
            self.conn = databases.mysql.MySQLConnection(config)

    def seed(self):
        for model in self.config["models"]:
            print(f"{model}: {self.config['models'][model]['fields']}")

    def template_func(self):
        print("Default")