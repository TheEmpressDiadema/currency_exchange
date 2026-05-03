from dataclasses import dataclass

@dataclass
class Currency:
    code: str
    full_name: str
    sign: str