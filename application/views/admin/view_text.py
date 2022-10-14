from crypt import methods
from app import db
from admin import admin
from models.text import Text
from flask import render_template, request, redirect, url_for


@admin.route('/text')
def text_admin():
    text_list = Text.query.all()
    return render_template('/admin/text/text.html', text_list=text_list)


@admin.route('/text_add', methods=['post','get'])
def text_add():
    if request.method == 'POST':
        text = Text()
        db.session.add(text)
        db.session.commit()
        return redirect(url_for('admin.text_admin'))

    text = Text()
    db.session.add(text)
    db.session.commit()
    return render_template('/admin/text/text_add.html', text=text)


@admin.route('/text_update_<int:id>', methods=('get','post'))
def text_update(id):
    text = Text.query.get(id)
    return render_template('/admin/text/text_update.html', text = text)


@admin.route('/text_delete_<int:id>')
def text_delete(id):
    text = Text.query.get(id)
    db.session.delete(text)
    db.session.commit()
    return redirect(url_for('admin.text_admin'))


@admin.route('/save_text_data', methods=['POST'])
def save_text_data():
    data = request.get_json()
    id = int(data['data']['id'])
    value = data['data']['value']
    text = Text.query.get(id)
    text.text = value

    db.session.commit()    
    return "", 201