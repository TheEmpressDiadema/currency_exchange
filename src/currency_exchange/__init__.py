from currency_exchange.model.model import CodePair, Currency, ExchangeRate
from currency_exchange.model.DAO.currencyDAO import CurrencyDAO
from currency_exchange.model.DAO.exchangeRateDAO import ExchangeRateDAO


def main() -> None:
    cur_dao = CurrencyDAO()
    print(cur_dao.insert(Currency(1, "AST", "African canadian Toller", "T")))