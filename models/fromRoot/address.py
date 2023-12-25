from typing import Any
from dataclasses import dataclass
from models.fromRoot.geo import Geo


@dataclass
class Address:
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo

    @staticmethod
    def from_dict(obj: Any) -> 'Address':
        _street = str(obj.get("street"))
        _suite = str(obj.get("suite"))
        _city = str(obj.get("city"))
        _zipcode = str(obj.get("zipcode"))
        _geo = Geo.from_dict(obj.get("geo"))
        return Address(_street, _suite, _city, _zipcode, _geo)
