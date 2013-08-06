# -*- coding: utf-8 -*-

import sys

from os.path import dirname, realpath

from bridge import app

reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(app.root_path)

#from nutrition.database import init_db
#init_db()

app.run(host='localhost', port=80, debug=True)
