# -*- coding: utf-8 -*-

import hashlib

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Binary, Table, ForeignKey, UniqueConstraint
from sqlalchemy.sql import text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship

from nutrition.database import T, talk

class Category(T):

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    pid = Column(Integer, index=True)
    name = Column(String(50), nullable=False)

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter(Category.name == name).first()
        #cid = cls.get_id_by_name(name)
        #return cls.get(cid)

    @classmethod
    def get_id_by_name(cls, name):
        pass

