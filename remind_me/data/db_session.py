from typing import Callable, Optional

import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
from decouple import config

from remind_me.data.modelbase import SqlAlchemyBase

__factory: Optional[Callable[[], Session]] = None


def global_init():
    global __factory
    if __factory:
        return
    conn_string = config('CONN_STRING')
    engine = sa.create_engine(conn_string, echo=False)
    __factory = orm.sessionmaker(bind=engine)
    import remind_me.data._all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory

    if not __factory:
        raise Exception('You must call global_init() before using this method')
    
    session: Session = __factory()
    session.expire_on_commit = False
    return session