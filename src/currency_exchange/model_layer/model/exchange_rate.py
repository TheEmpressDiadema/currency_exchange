from dataclasses import dataclass

@dataclass
class ExchangeRate:
    base_currency_id: int
    target_currency_id: int
    rate: float