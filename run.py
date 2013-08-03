# -*- coding: utf-8 -*-

import sys

from os.path import dirname, realpath

from bridge import app

reload(sys)
sys.setdefaultencoding('utf8') 
sys.path.append(app.root_path)

app.run(host='localhost', port=80, debug=True)
