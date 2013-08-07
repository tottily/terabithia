# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import text

from nutrition.database import Base

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

class Url(Base):

    __tablename__ = 'url'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    refresh_time = Column(DateTime, server_default=text('NOW()'))
