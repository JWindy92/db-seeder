import yaml
import databases.dbwrapper

def load_config():
    with open("config.yml", "r") as config:
        data = yaml.load(config, Loader=yaml.FullLoader)

    return data


class Seeder:
    def __init__(self):
        config = load_config()
        self.databases = config['databases']

    def seed_dbs(self):
        for db in self.databases:
            print(f"Seeding {db}")
            config = self.databases[db]
            conn = databases.dbwrapper.DbConnection(config)
            conn.seed()
            conn.template_func()


if __name__ == '__main__':

    seeder = Seeder()
    seeder.seed_dbs()

