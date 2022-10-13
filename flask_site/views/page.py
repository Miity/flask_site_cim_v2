from crypt import methods
from app import app, page_not_found
from models.page import Page
from flask import render_template



@app.route('/page/<slug>')
def detail(slug):
    page = Page.query.where(Page.slug == slug).first()
    if page and page.archive == False:
        return render_template('user/page/page_detail.html', page=page)
    return page_not_found('page not found')

