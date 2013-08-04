# -*- coding: utf-8 -*-

import os

from flask import Flask, send_from_directory
from river import home, admin
from nutrition.config import TERABITHIA_GLOBALS

app = Flask('Terabithia', template_folder="plant", static_folder='flower')
app.jinja_env.globals.update(TERABITHIA_GLOBALS)

rivers = {
    home: '',
    admin: '/admin',
}

for router, prefix in rivers.items():
    app.register_blueprint(router, url_prefix=prefix)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'flower'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
