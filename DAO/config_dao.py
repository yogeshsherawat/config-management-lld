from DB import DB

class ConfigDAO:
    def __init__(self, db):
        self.db = db

    @staticmethod
    def get_config_by_name(name):
        config = DB.config_name_to_config[name]
        return config

    @staticmethod
    def add_config(name, data):
        config = DB.config_name_to_config[name] = data
        return config

    @staticmethod
    def delete_config_by_name(name):
        del DB.config_name_to_config[name]

    @staticmethod
    def get_all_config_names():
        return list(DB.config_name_to_config.keys())

