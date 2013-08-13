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
    comment = Column(String(50))
    refresh_time = Column(DateTime, server_default=text('NOW()'))

    def update(self):
        md5 = hashlib.md5(self.url).hexdigest()
        if md5 != self.md5:
            self.md5 = md5
        self.refresh_time = datetime.now()
        return super(Url, self).update()

    @classmethod
    def add(cls, **kwargs):
        url = kwargs.get('url')
        if not url: return None
        kwargs['md5'] = hashlib.md5(url).hexdigest()
        return super(Url, cls).add(**kwargs)

    @classmethod
    def get_by_url(cls, url):
        md5 = hashlib.md5(url).hexdigest()
        return cls.query.filter(cls.md5 == md5).first()
