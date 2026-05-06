import sqlite3

from currency_exchange.model.model import ExchangeRate, CodePair
from currency_exchange.model.DAO.abstractDAO import AbstractDAO

class ExchangeRateDAO(AbstractDAO):

    def insert(self, exchange_rate: ExchangeRate) -> ExchangeRate:
        with sqlite3.connect(self._DATABASE_PATH) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO exchange_rate(base_currency_id, target_currency_id, rate) VALUES (?,?,?) RETURNING *"
            params = (
                exchange_rate.base_currency_id,
                exchange_rate.target_currency_id,
                exchange_rate.rate
            )
            cursor.execute(query, params)
            result = cursor.fetchone()
            cursor.close()
            return ExchangeRate(*result)

    def update(self, exchange_rate: ExchangeRate, code_pair: CodePair):
        with sqlite3.connect(self._DATABASE_PATH) as connection:
            cursor = connection.cursor()
            query = """
            UPDATE exchange_rate
            SET id=?, target_currency_id=?, rate=?
            WHERE base_currency_id=(SELECT id FROM currency WHERE code=?) AND
            target_currency_id=(SELECT id FROM currency WHERE code=?)
            RETURNING *
            """
            params = (
                exchange_rate.base_currency_id, 
                exchange_rate.target_currency_id,
                exchange_rate.rate,
                code_pair.base_currency_code,
                code_pair.target_currency_code)
            cursor.execute(query, params)

    def delete_by_id(self, id: int):
        with sqlite3.connect(self._DATABASE_PATH) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM exchange_rate WHERE id=?"
            cursor.execute(query, (id, ))
            cursor.close()

    def get_by_id(self, id: int) -> ExchangeRate:
        with sqlite3.connect(self._DATABASE_PATH) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM exchange_rate WHERE id=?"
            cursor.execute(query, (id, ))
            result = cursor.fetchone()
            cursor.close()
            return ExchangeRate(*result)
    
    def get_all(self) -> list[ExchangeRate]:
        with sqlite3.connect(self._DATABASE_PATH) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM exchange_rate"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return [ExchangeRate(*el) for el in result]
        
    def get_by_code_pair(self, code_pair: CodePair) -> ExchangeRate:
        with sqlite3.connect(self._DATABASE_PATH) as connection:
            cursor = connection.cursor()
            query = """
            SELECT * FROM exchange_rate WHERE 
            base_currency_id=(SELECT id FROM currency WHERE code=?) AND
            target_currency_id=(SELECT id FROM currency WHERE code=?)
            """
            cursor.execute(query, (code_pair.base_currency_code, code_pair.target_currency_code))
            result = cursor.fetchone()
            cursor.close()
            return ExchangeRate(*result)