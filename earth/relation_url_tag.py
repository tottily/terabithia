# -*- coding: utf-8 -*-

import hashlib

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Binary, Table, ForeignKey, UniqueConstraint
from sqlalchemy.sql import text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship

from nutrition.database import T

class UserUrlTagRelation(T):

    __tablename__ = 'relation_user_url_tag'
    __table_args__ = (
        UniqueConstraint('user_id', 'tag_id', 'url_id', name='uix_url_tag_user'),
    )

    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', Integer, ForeignKey('user.id'))
    tag_id = Column('tag_id', Integer, ForeignKey('tag.id'))
    url_id = Column('url_id', Integer, ForeignKey('url.id'))

    urls = relationship("Url", backref="urls")

