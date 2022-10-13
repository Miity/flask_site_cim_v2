from crypt import methods
from app import db
from models.page import Page
from admin import admin
from flask import render_template, request
from slugify import slugify


#### pages info
@admin.route('page_admin')
def page_admin():
    return render_template('admin/page/page.html')

@admin.route('load_pages_info', methods=['get'])
def load_pages_info():
    pages = Page.query.all()
    template = render_template('admin/page/pages_info.html', pages=pages)
    return {'template': template}

@admin.route('/page_add/', methods=["GET", "POST"])
def page_add():
    page = Page()
    db.session.add(page)
    db.session.commit()
    return render_template('admin/page/page_update.html', page=page)


### update page
@admin.route('/page_update/<id>/')
def page_update(id):
    page = Page.query.get(id)
    return render_template('admin/page/page_update.html', page=page)

@admin.route('/load_page_info/<int:id>/', methods=['get'])
def load_page_info(id):
    page = Page.query.get(id)
    template = render_template('admin/page/page_info.html', page=page)
    return {'template': template}


@admin.route('/page_update_ajax', methods=['post'])
def page_update_ajax():
    data = request.get_json()
    page = Page.query.get(int(data['page']['id']))

    if 'slug' in data['page']:
        if slugify(data['page']['slug'])== '':
            return ('slug errore',500)
        if data['page']['slug'] == '' or data['page']['slug'] == None:
            return ('slug errore',500)
        page.slug = slugify(data['page']['slug'])

    elif 'title' in data['page']:
        page.title = data['page']['title']

    elif 'description' in data['page']:
        page.description = data['page']['description']

    elif 'archive' in data['page']:
        if data['page']['archive'] == True:
            page.delete()
        elif data['page']['archive'] == False:
            if page.title == '' or page.title == None:
                return ('check page title and slug',500)
            elif page.slug == '' or page.slug == None:
                page.slug = slugify(page.title)
            page.archive = False

    db.session.commit()
    return ('',201)
