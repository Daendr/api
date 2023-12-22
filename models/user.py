from typing import Any
from dataclasses import dataclass
from models.fromRoot.address import Address
from models.fromRoot.company import Company


@dataclass
class User:
    id: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        _id = int(obj.get("id"))
        _name = str(obj.get("name"))
        _username = str(obj.get("username"))
        _email = str(obj.get("email"))
        _address = Address.from_dict(obj.get("address"))
        _phone = str(obj.get("phone"))
        _website = str(obj.get("website"))
        _company = Company.from_dict(obj.get("company"))
        return User(_id, _name, _username, _email, _address, _phone, _website, _company)
