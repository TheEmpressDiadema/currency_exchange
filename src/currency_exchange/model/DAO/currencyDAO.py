import sqlite3

from currency_exchange.model.model import Currency
from currency_exchange.model.DAO.abstractDAO import AbstractDAO

class CurrencyDAO(AbstractDAO):
    
    def insert(self):
        pass

    def update(self):
        pass

    def delete_by_id(self):
        pass

    def delete_by_code(self):
        pass

    def get_by_id(self, id: int) -> Currency:
        with sqlite3.connect(self._DATABASE_PATH) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM currency WHERE id=?"
            cursor.execute(query, (id, ))
            result = cursor.fetchone()
            cursor.close()
            return result
    
    def get_all(self) -> list[Currency]:
        with sqlite3.connect(self._DATABASE_PATH) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM currency"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
    
    def get_by_code(self, code: str) -> Currency:
        with sqlite3.connect(self._DATABASE_PATH) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM currency WHERE code=?"
            cursor.execute(query, (code, ))
            result = cursor.fetchone()
            cursor.close()
            return result