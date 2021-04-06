from typing import Optional
import hashlib
import uuid

from remind_me.data.user import User


def hash_string(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_string(hashed_password, entered_password):
    password, salt = hashed_password.split(':')
    print(f'Password: {password}')
    val = hashlib.sha256(salt.encode() + entered_password.encode()).hexdigest()
    print(f'Val: {val}')
    return password == hashlib.sha256(salt.encode() + entered_password.encode()).hexdigest()


def create_account(name: str, email: str, password: str) -> User:
    password = hash_string(password)
    return User(name, email, password)



