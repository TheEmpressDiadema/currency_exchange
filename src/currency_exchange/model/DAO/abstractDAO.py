from abc import ABC, abstractmethod 

class AbstractDAO(ABC):

    _DATABASE_PATH = r"src\currency_exchange\data\db\data.db"

    @abstractmethod
    def get_by_id(self, id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def delete_by_id(self, id: int):
        pass