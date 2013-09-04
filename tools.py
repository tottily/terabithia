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
from earth.url import Url
from earth.relation_url_category import UrlCategoryRelation

URLS = []

def add_category():
    categories = ['新闻', '搜索', '社区', '视频', '购物', '邮箱']
    for cat in categories:
        Category.add(name=cat)

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
        u = Url.add(name=name, url=url)
        for cat in cates:
            cat = Category.get_by_name(cat)
            #UrlCategoryRelation.add(url_id=u.id, category_id=cat.id)
            #UrlCategoryRelation(url_id=u.id, category_id=cat.id)
            print u.categories
            u.categories.append(cat)
        print u.tags
        print u.categories

def fillup():
    add_category()
    add_url()

if __name__ == "__main__":
    fillup()
