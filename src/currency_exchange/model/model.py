from dataclasses import dataclass


@dataclass
class Currency:

    id: int
    code: str
    full_name: str
    sign: str

@dataclass
class ExchangeRate:

    id: int
    base_currency_id: int
    target_currency_id: int
    rate: int