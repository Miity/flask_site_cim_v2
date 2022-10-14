from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Configuration


app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)


from blocks import block
from admin import admin
app.register_blueprint(block, url_prefix='/block')
app.register_blueprint(admin, url_prefix='/admin')



################ VIEW
from flask import render_template
from models.image import Gallery



@app.route('/')
def index():
    return render_template("user/index.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('user/page_not_found.html')

@app.errorhandler(405)
def page_not_found_405(error):
    return render_template('user/page_not_found.html')



# static pages
@app.route('/partfolio')
def partfolio():
    gallery = Gallery.query.filter_by(title = 'Portfolio').first()
    return render_template('user/partfolio.html', gallery=gallery)