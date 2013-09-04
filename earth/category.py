# -*- coding: utf-8 -*-

import hashlib

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Binary, Table, ForeignKey, UniqueConstraint
from sqlalchemy.sql import text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship

from nutrition.database import T
from earth.relation_url_category import RelationUrlCategory

class Category(T):

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    pid = Column(Integer, index=True)
    name = Column(String(50), nullable=False, index=True)

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter(Category.name == name).first()

    def _relations(self, limit):
        return RelationUrlCategory.query.filter(RelationUrlCategory.category_id == self.id).limit(limit)

    def urls(self, limit=10):
        from earth.url import Url
        relations = self._relations(limit)
        ids = [relation.url_id for relation in relations]
        return Url.get_multi(ids)
