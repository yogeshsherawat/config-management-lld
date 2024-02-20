from DAO import ConfigDAO


class ConfigService:

    def __init__(self, search_client):
        self.config_search_client = search_client

    def get_config(self, name):
        return ConfigDAO.get_config_by_name(name)

    def add_config(self, name, data):
        return ConfigDAO.add_config(name, data)

    def delete_config(self, name):
        return ConfigDAO.delete_config_by_name(name)

    def search_config(self, name):
        return self.config_search_client.search(name)
