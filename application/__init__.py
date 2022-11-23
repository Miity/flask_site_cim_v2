from application.config import Configuration
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

import application.views.page
from application.blueprints import admin, block
app.register_blueprint(block, url_prefix='/block')
app.register_blueprint(admin, url_prefix='/admin')
