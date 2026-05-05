import sqlite3

from currency_exchange.model.model import ExchangeRate
from currency_exchange.model.DAO.abstractDAO import AbstractDAO


class ExchangeRateDAO(AbstractDAO):

    def insert(self):
        pass

    def update(self):
        pass

    def delete_by_id(self):
        pass

    def delete_by_code_pair(self):
        pass

    def get_by_id(self, id: int) -> ExchangeRate:
        with sqlite3.connect(self._DATABASE_PATH) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM exchange_rate WHERE id=?"
            cursor.execute(query, (id, ))
            result = cursor.fetchone()
            cursor.close()
            return result
    
    def get_all(self) -> list[ExchangeRate]:
        with sqlite3.connect(self._DATABASE_PATH) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM exchange_rate"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        
    def get_by_code_pair(self, pair: tuple[str]) -> ExchangeRate:
        with sqlite3.connect(self._DATABASE_PATH) as connection:
            cursor = connection.cursor()
            query = """
            SELECT * FROM exchange_rate WHERE 
            base_currency_id=(SELECT id FROM currency WHERE code=?) and
            target_currency_id=(SELECT id FROM currency WHERE code=?)
            """
            cursor.execute(query, pair)
            result = cursor.fetchone()
            cursor.close()
            return result