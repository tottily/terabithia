# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError

from nutrition.database import Base, talk

class T(object):

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
