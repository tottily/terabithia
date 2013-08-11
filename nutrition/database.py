# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from nutrition.config import DB_CONFIG

DB_ENGINE = create_engine(
    'mysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_CONFIG['USER'], DB_CONFIG['PASSWORD'], DB_CONFIG['HOST'], DB_CONFIG['PORT'], DB_CONFIG['DB_NAME']),
    isolation_level="READ COMMITTED",
    convert_unicode=True,
    echo=DB_CONFIG['ECHO'],
)

_db_session = sessionmaker(autocommit=False, autoflush=False, bind=DB_ENGINE)
talk = scoped_session(_db_session)

Base = declarative_base()
Base.query = talk.query_property()

def establish_database(force=False):
    if force:
        destroy_database()
    from earth.url import Url, UrlCategoryRelation, UserUrlTagRelation
    from earth.user import User
    from earth.tag import Tag
    from earth.category import Category
    Base.metadata.create_all(bind=DB_ENGINE)

def destroy_database():
    from earth.url import Url, UrlCategoryRelation, UserUrlTagRelation
    from earth.user import User
    from earth.tag import Tag
    from earth.category import Category
    talk.remove()
    Base.metadata.drop_all(bind=DB_ENGINE)

class T(Base):

    __abstract__ = True

    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    def __repr__(self):
        return '%r' % (self.__class__)

    def delete(self):
        talk.delete(self)
        return talk.commit()

    def update(self):
        try:
            talk.commit()
            return True
        except IntegrityError:
            talk.rollback()
            return False

    @classmethod
    def add(cls, **kwargs):
        obj = cls(**kwargs)
        try:
            talk.add(obj)
            talk.commit()
            talk.refresh(obj)
            return obj
        except IntegrityError:
            return None

    @classmethod
    def get(cls, id):
        return cls.query.get(id)

    @classmethod
    def gets(cls, ids):
        return [cls.get(id) for id in ids]
