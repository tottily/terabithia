# -*- coding: utf-8 -*-

import hashlib

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Binary, Table, ForeignKey, UniqueConstraint
from sqlalchemy.sql import text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship

from nutrition.database import T

class Url(T):

    __tablename__ = 'url'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    url = Column(String(2048), nullable=False)
    md5 = Column(String(32), nullable=False, unique=True)
    total = Column(Integer, index=True)
    comment = Column(String(50))
    refresh_time = Column(DateTime, server_default=text('NOW()'))

class UrlCategoryRelation(T):

    __tablename__ = 'relation_url_category'
    __table_args__ = (
        UniqueConstraint('url_id', 'category_id', name='uix_url_category'),
    )

    id = Column('id', Integer, primary_key=True)
    url_id = Column('url_id', Integer)
    category_id = Column('category_id', Integer)

class UserUrlTagRelation(T):

    __tablename__ = 'relation_user_url_tag'
    __table_args__ = (
        UniqueConstraint('user_id', 'tag_id', 'url_id', name='uix_url_tag_user'),
    )

    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', Integer)
    tag_id = Column('tag_id', Integer, index=True)
    url_id = Column('url_id', Integer, index=True)

