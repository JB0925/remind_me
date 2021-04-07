from typing import Optional
import hashlib
import uuid

from passlib.handlers.sha2_crypt import sha512_crypt as crypto

from remind_me.data.user import User
from remind_me.data import db_session




def hash_password(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, entered_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + entered_password.encode()).hexdigest()


def create_account(name: str, email: str, password: str) -> User:
    session = db_session.create_session()

    try:
        user = User()
        user.name = name
        user.email = email
        user.hashed_password = crypto.hash(password, rounds=172_434)

        session.add(user)
        session.commit()
        return user

    finally:
        session.close()


def login_user(name: str, password: str) -> Optional[User]:
    session = db_session.create_session()

    try:
        user = session.query(User).filter(User.name == name).first()
        if not user:
            return user
        
        if not crypto.verify(password, user.hashed_password):
            return None
        
        return user
    finally:
        session.close()


def make_job(event: str, number: str, carrier:str, date: str):
    return [(event, number, carrier, date)]


def store_events(email, phone_number, carrier, event, date_and_time, user_id):
    session = db_session.create_session()

    try:
        user = session.query(User).filter(User.email == email).first()


