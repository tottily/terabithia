# -*- coding: utf-8 -*-

import sys

from os.path import dirname, realpath

from bridge import app

reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(app.root_path)

from nutrition.database import establish_database
establish_database(force=True)
