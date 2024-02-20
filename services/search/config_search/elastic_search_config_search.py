from .i_config_search import IConfigSearch


class Elasticsearch:
    def __init__(self, config):
        self.config = config


class ElasticSearchConfigSearch(IConfigSearch):
    def __init__(self):
        self.host = "localhost"
        self.port = 9200
        self.index = "config_search"
        self.doc_type = "config"
        self.url = "http://" + self.host + ":" + str(self.port) + "/" + self.index + "/" + self.doc_type + "/"
        self.client = Elasticsearch([{'host': self.host, 'port': self.port}])

    def search(self, name):
        query = {
            "query": {
                "match": {
                    "name": name
                }
            }
        }
        return self.client.search(index=self.index, body=query)
