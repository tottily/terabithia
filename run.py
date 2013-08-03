# -*- coding: utf-8 -*-

import sys

from os.path import dirname, realpath

from bridge import app

sys.path.append(app.root_path)

print app.url_map
app.run(host='localhost', port=80, debug=True)
