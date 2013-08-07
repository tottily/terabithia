# -*- coding: utf-8 -*-

import hashlib

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Binary
from sqlalchemy.sql import text
from sqlalchemy.exc import IntegrityError

from nutrition.database import Base, talk

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

class Site(Base):

    __tablename__ = 'site'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    url = Column(String(2048), nullable=False)
    md5 = Column(String(32), nullable=False, unique=True)
    refresh_time = Column(DateTime, server_default=text('NOW()'))

    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.md5 = hashlib.md5(url).hexdigest()

    def __repr__(self):
        return '<%r %r>' % (self.__class__, self.name)

    def delete(self):
        talk.delete(self)
        return talk.commit()

    def update(self, name=None, url=None):
        if not name and not url:
            return False
        updated = False
        if name and name != self.name:
            self.name = name
            updated = True
        if url and url != self.url:
            self.url = url
            self.md5 = hashlib.md5(url).hexdigest()
            updated = True
        if updated:
            self.refresh_time = datetime.now()
            # TODO when md5 exist, rollback
            return talk.commit()
        else:
            return False

    @classmethod
    def add(cls, name, url):
        site = Site(name, url)
        try:
            talk.add(site)
            talk.commit()
        except IntegrityError:
            return None

    @classmethod
    def get(cls, id):
        return Site.query.get(id)
