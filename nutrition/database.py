# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_engine = create_engine(
    'mysql://root:@localhost/test',
    isolation_level="READ COMMITTED"
)

_db_session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
db_session = scoped_session(_db_session)

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    from earth.url import Url
    Base.metadata.create_all(bind=db_engine)
