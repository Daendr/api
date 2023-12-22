from typing import Any
from dataclasses import dataclass


@dataclass
class Company:
    name: str
    catchPhrase: str
    bs: str

    @staticmethod
    def from_dict(obj: Any) -> 'Company':
        _name = str(obj.get("name"))
        _catchPhrase = str(obj.get("catchPhrase"))
        _bs = str(obj.get("bs"))
        return Company(_name, _catchPhrase, _bs)
