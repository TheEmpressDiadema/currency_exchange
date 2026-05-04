from dataclasses import dataclass

@dataclass
class Currency:
    id: int
    code: str
    full_name: str
    sign: str