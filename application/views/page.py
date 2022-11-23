from crypt import methods
from application import app
from application.views import page_not_found
from application.models.page import Page
from flask import render_template


@app.route('/page/<slug>')
def detail(slug):
    page = Page.query.where(Page.slug == slug).first()
    if page and page.archive == False:
        return render_template('user/page/page_detail.html', page=page)
    return page_not_found('page not found')
