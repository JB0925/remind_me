from typing import Optional
import hashlib
import uuid

from remind_me.data.user import User


def hash_password(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, entered_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + entered_password.encode()).hexdigest()


def create_account(name: str, email: str, password: str) -> User:
    password = hash_password(password)
    return User(name, email, password)


def login_user(name: str, password: str) -> Optional[User]:
    pw = hash_password(password)
    if check_password(pw, password):
        return User('test', 'test_email', 'pw')
    return None


def make_job(event: str, number: str, carrier:str, date: str):
    return [(event, number, carrier, date)]


