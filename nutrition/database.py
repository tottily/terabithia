# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from nutrition.config import DB_CONFIG

db_engine = create_engine(
    'mysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_CONFIG['USER'], DB_CONFIG['PASSWORD'], DB_CONFIG['HOST'], DB_CONFIG['PORT'], DB_CONFIG['DB_NAME']),
    isolation_level="READ COMMITTED",
    convert_unicode=True,
)

_db_session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
talk = scoped_session(_db_session)

Base = declarative_base()
Base.query = talk.query_property()

def init_db():
    from earth.url import *
    Base.metadata.create_all(bind=db_engine)
