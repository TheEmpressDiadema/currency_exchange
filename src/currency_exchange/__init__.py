from currency_exchange.model.DAO.currencyDAO import CurrencyDAO
from currency_exchange.model.DAO.exchangeRateDAO import ExchangeRateDAO

def main() -> None:
    cur_dao = CurrencyDAO()
    exchange_rate_dao = ExchangeRateDAO()
    print(cur_dao.get_by_id(1))
    print(cur_dao.get_all())
    print(cur_dao.get_by_code("EUR"))
    print("здесь будут эксченжрэйт")
    print(exchange_rate_dao.get_all())
    print(exchange_rate_dao.get_by_id(1))
    print(exchange_rate_dao.get_by_code_pair(("EUR", "USD")))
