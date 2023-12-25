from typing import Any
from dataclasses import dataclass


@dataclass
class Root:
    userId: int
    id: int
    title: str
    body: str

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _userId = int(obj.get("userId"))
        _id = int(obj.get("id"))
        _title = str(obj.get("title"))
        _body = str(obj.get("body"))
        return Root(_userId, _id, _title, _body)
