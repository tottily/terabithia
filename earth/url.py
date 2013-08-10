# -*- coding: utf-8 -*-

import hashlib

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Binary, Table, ForeignKey, UniqueConstraint
from sqlalchemy.sql import text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship

from nutrition.database import Base

from earth.T import T

DEFAULT_URLS = (
    ('社区', [1, 2, 3]),
    ('新闻', [4, 5, 6]),
    ('搜索', [7, 8]),
)

URLS = {
    1: {'name': '豆瓣', 'url': 'http://www.douban.com'},
    2: {'name': '猫扑', 'url': 'http://www.mop.com'},
    3: {'name': '天涯', 'url': 'http://www.tianya.cn'},
    4: {'name': '网易', 'url': 'http://www.163.com'},
    5: {'name': '', 'url': ''},
    6: {'name': '', 'url': ''},
    7: {'name': '百度', 'url': 'http://www.baidu.com'},
    8: {'name': '', 'url': ''},
}

class UrlCategoryRelation(T, Base):

    __tablename__ = 'relation_url_category'
    __table_args__ = (
        UniqueConstraint('url_id', 'category_id', name='uix_url_category'),
    )

    id = Column('id', Integer, primary_key=True)
    url_id = Column('url_id', Integer)
    category_id = Column('category_id', Integer)

class Category(T, Base):

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    pid = Column(Integer, index=True)
    name = Column(String(50), nullable=False)

class Tag(T, Base):

    __tablename__ = 'tag'
    __table_args__ = (
        UniqueConstraint('name', name='uix_name'),
    )

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

class UserUrlTagRelation(T, Base):

    __tablename__ = 'relation_user_url_tag'
    __table_args__ = (
        UniqueConstraint('user_id', 'tag_id', 'url_id', name='uix_url_tag_user'),
    )

    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', Integer)
    tag_id = Column('tag_id', Integer, index=True)
    url_id = Column('url_id', Integer, index=True)

class Url(T, Base):

    __tablename__ = 'url'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    url = Column(String(2048), nullable=False)
    md5 = Column(String(32), nullable=False, unique=True)
    total = Column(Integer, index=True)
    comment = Column(String(50))
    refresh_time = Column(DateTime, server_default=text('NOW()'))

class User(T, Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(1024))
    reg_time = Column(DateTime, server_default=text('NOW()'))
