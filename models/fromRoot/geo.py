from typing import Any
from dataclasses import dataclass


@dataclass
class Geo:
    lat: str
    lng: str

    @staticmethod
    def from_dict(obj: Any) -> 'Geo':
        _lat = str(obj.get("lat"))
        _lng = str(obj.get("lng"))
        return Geo(_lat, _lng)
