# -*- coding: utf-8 -*-

import sys

from os.path import dirname, realpath

from bridge import app

reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(app.root_path)

from nutrition.database import init_db, talk
init_db()

from earth.url import *
url = Url.add(name='豆瓣', url='http://www.douban.com', md5='5')

category = Category.add(name='社区')

relation = UrlCategoryRelation.add(url_id=url.id, category_id=category.id)

url = Url.add(name='猫扑', url='http://www.mop.com', md5='10')
relation = UrlCategoryRelation.add(url_id=url.id, category_id=category.id)
print url, category, relation


user = User.add(name='totty', email='totty.com.cn@gmail.com')
print user, user.id

tag = Tag.add(name='喜欢')

UserUrlTagRelation.add(user_id=user.id, tag_id=tag.id, url_id=url.id)
