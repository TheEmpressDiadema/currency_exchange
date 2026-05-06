import sqlite3

from currency_exchange.model.model import Currency
from currency_exchange.model.DAO.abstractDAO import AbstractDAO

class CurrencyDAO(AbstractDAO):
    
    def insert(self, currency: Currency) -> Currency:
        with sqlite3.connect(self._DATABASE_PATH) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO currency(code, full_name, sign) VALUES (?,?,?) RETURNING *"
            params = (currency.code, currency.full_name, currency.sign)
            cursor.execute(query, params)
            result = cursor.fetchone()
            cursor.close()
            return Currency(*result)

    def delete_by_id(self, id: int):
        with sqlite3.connect(self._DATABASE_PATH) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM currency WHERE id=?"
            cursor.execute(query, (id,))
            cursor.close()

    def get_by_id(self, id: int) -> Currency:
        with sqlite3.connect(self._DATABASE_PATH) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM currency WHERE id=?"
            cursor.execute(query, (id, ))
            result = cursor.fetchone()
            cursor.close()
            return Currency(*result)
    
    def get_all(self) -> list[Currency]:
        with sqlite3.connect(self._DATABASE_PATH) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM currency"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return [Currency(*element) for element in result]
    
    def get_by_code(self, code: str) -> Currency:
        with sqlite3.connect(self._DATABASE_PATH) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM currency WHERE code=?"
            cursor.execute(query, (code, ))
            result = cursor.fetchone()
            cursor.close()
            return Currency(*result)