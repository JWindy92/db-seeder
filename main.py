import yaml
import databases.mongo
import databases.mysql

def load_config():
    with open("config.yml", "r") as config:
        data = yaml.load(config, Loader=yaml.FullLoader)

    return data


class Seeder:
    def __init__(self):
        config = load_config()
        self.database = config['database']
        self.models = config['models']

        self.connect_to_db()

    def connect_to_db(self):
        print(self.database['engine'])
        if self.database['engine'] == "mongo":
            databases.mongo.connect()
        elif self.database['engine'] == "mysql":
            databases.mysql.connect()
        else:
            print("Unsupported database engine")

if __name__ == '__main__':

    seeder = Seeder()

