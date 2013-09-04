# -*- coding: utf-8 -*-

import hashlib

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Binary, Table, ForeignKey, UniqueConstraint
from sqlalchemy.sql import text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship

from nutrition.database import T

class RelationUrlCategory(T):

    __tablename__ = 'relation_url_category'
    __table_args__ = (
        UniqueConstraint('url_id', 'category_id', name='uix_url_category'),
    )

    id = Column('id', Integer, primary_key=True)
    url_id = Column('url_id', Integer, index=True)
    category_id = Column('category_id', Integer, index=True)

