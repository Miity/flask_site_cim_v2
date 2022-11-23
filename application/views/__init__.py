from application import app
from flask import render_template
from application.models.image import Gallery


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