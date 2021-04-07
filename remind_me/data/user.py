from datetime import datetime

import sqlalchemy as sa

from remind_me.data.modelbase import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, index=True, unique=True)
    email = sa.Column(sa.String, index=True, unique=True)
    hashed_password = sa.Column(sa.String)
    # def __init__(self, name, email, hashed_password) -> None:
    #     self.id = 1
    #     self.name = name
    #     self.email = email
    #     self.hashed_password = hashed_password