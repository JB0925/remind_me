from datetime import datetime


class User:
    def __init__(self, name, email, hashed_password) -> None:
        self.id = 1
        self.name = name
        self.email = email
        self.hashed_password = hashed_password