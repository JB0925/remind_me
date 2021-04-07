import sqlalchemy as sa
from sqlalchemy import orm 

from remind_me.data.modelbase import SqlAlchemyBase



class Events(SqlAlchemyBase):

    __tablename__ = 'events'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    phone_number = sa.Column(sa.String, index=True, unique=True)
    carrier = sa.Column(sa.String)
    event = sa.Column(sa.String, index=True)
    date_and_time = sa.Column(sa.String, index=True)

    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    user = orm.relation('User')

    
    def __str__(self):
        return f'Id: {self.id}, Number: {self.phone_number}, Carrier: {self.carrier}, Event: {self.event}, Remind Date: {self.date_and_time}, User Id: {self.user_id}'