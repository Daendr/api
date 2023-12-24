class UserModel:
    def __init__(self, id, name, username, email, address, phone, website, company):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.address = address
        self.phone = phone
        self.website = website
        self.company = company

    def __eq__(self, other):
        return (
            isinstance(other, UserModel) and
            self.id == other.id and
            self.name == other.name and
            self.username == other.username and
            self.email == other.email and
            self.address == other.address and
            self.phone == other.phone and
            self.website == other.website and
            self.company == other.company
        )
