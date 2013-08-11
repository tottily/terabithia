# -*- coding: utf-8 -*-

import hashlib

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Binary, Table, ForeignKey, UniqueConstraint
from sqlalchemy.sql import text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship

from nutrition.database import T

class Tag(T):

    __tablename__ = 'tag'
    __table_args__ = (
        UniqueConstraint('name', name='uix_name'),
    )

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter(cls.name==name).first()
