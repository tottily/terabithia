# -*- coding: utf-8 -*-

import sys

from os.path import dirname, realpath

from bridge import app

reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(app.root_path)

from nutrition.database import init_db, talk
init_db()

from earth.site import Site
site = Site.get(6)
site.update(name='何义', url='http://www.dougun.com')
