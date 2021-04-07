from datetime import datetime

import sqlalchemy as sa

from remind_me.data.modelbase import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, index=True, unique=True)
    email = sa.Column(sa.String, index=True, unique=True)
    hashed_password = sa.Column(sa.String)
    

    def __str__(self):
        return f'Id: {self.id}, Name: {self.name}, Email: {self.email}, Hashed Password: {self.hashed_password}'