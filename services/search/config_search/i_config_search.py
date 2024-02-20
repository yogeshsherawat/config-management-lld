from abc import abstractmethod, ABC

class IConfigSearch(ABC):

    @abstractmethod
    def search(self, name):
        pass