from .i_config_search import IConfigSearch
from DAO import ConfigDAO


class InMemoryConfigSearch(IConfigSearch):

    """
    Either we can load all the data in memory, or we can use memecache here to keep data in memory.
    """

    def search(self, name):
        all_config_names = ConfigDAO.get_all_config_names()
        found_results = []
        for config_name in all_config_names:
            if name in config_name:
                found_results.append(ConfigDAO.get_config_by_name(config_name))
        return found_results
