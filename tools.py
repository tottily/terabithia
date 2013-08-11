# -*- coding: utf-8 -*-

import sys
import hashlib

from os.path import dirname, realpath

from bridge import app

reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(app.root_path)

from nutrition.database import establish_database
establish_database(force=True)

from earth.category import Category
from earth.url import Url, UrlCategoryRelation

CATEGORIES = {}
URLS = []

def add_category():
    categories = ['新闻', '搜索', '社区', '视频', '购物', '邮箱']
    for cat in categories:
        c = Category.add(name=cat)
        CATEGORIES[cat] = c

def add_url():
    urls = [
        ('豆瓣', 'http://www.douban.com', ['社区']),
        ('网易', 'http://www.163.com', ['新闻', '邮箱']),
        ('百度', 'http://www.baidu.com', ['搜索']),
        ('淘宝', 'http://www.taobao.com', ['购物']),
        ('优酷', 'http://www.youku.com', ['视频']),
        ('Google', 'http://www.google.com', ['搜索']),
    ]
    for name, url, cates in urls:
        u = Url.add(name=name, url=url, md5=hashlib.md5(url).hexdigest())
        for cat in cates:
            cat = CATEGORIES.get(cat)
            UrlCategoryRelation.add(url_id=u.id, category_id=cat.id)

def fillup():
    add_category()
    add_url()

if __name__ == "__main__":
    fillup()
