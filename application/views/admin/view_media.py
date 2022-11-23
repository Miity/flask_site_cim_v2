from application import db
from application.models.image import Gallery, Image
from application.blueprints.admin import admin
from flask import render_template, request, redirect, flash, url_for
from werkzeug.utils import secure_filename
from application.models.image import gallery_images
from sqlalchemy import update
from application.views.media import new_image, new_gallery
import json


# --------------    GAllERY and Image index pages    -----------------

@admin.route("/images")
def image_admin():
    images = Image.query.all()
    return render_template('admin/image/image.html', images=images)

@admin.route("/gallery")
def gallery_admin():
    galleries = Gallery.query.all()
    return render_template('admin/image/gallery.html', galleries=galleries)


@admin.route('/gallery_add', methods=['get','post'])
def gallery_add():
    if request.method == "POST":    
        title = request.form['title']
        files = request.files.getlist('files')
        new_gallery(title, files)
        return redirect('/admin/gallery')
    return render_template('admin/image/gallery_add.html')

@admin.route('/image_add', methods=['post', 'get'])
def image_add():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if request.form['alt']:
            alt = request.form['alt']
        else:
            alt = file.filename.strip('.')[0]
        new_image(file, alt)

        return redirect(url_for('admin.image_admin'))
    return render_template('admin/image/image_add.html')


def del_obj(Cls):
    if request.method == 'DELETE':
        id = json.loads(request.get_json())['id']
        obj = Cls.query.get(id)
        obj.delete()
        flash('Object was deleted')

@admin.route('/gal/delete', methods=['DELETE'])
def gallery_delete():
    del_obj(Gallery)
    return '',200

@admin.route('/img/delete', methods=['DELETE'])
def image_delete():
    del_obj(Image)
    return '',200



# --------------    GALLERY UPDATE    -----------------

@admin.route('/gal_update/<int:id>')
def gallery_update(id):
    gal = Gallery.query.get(id)
    return render_template('admin/image/gallery_update.html', gallery=gal)


@admin.route('/rm_img_<int:img_id>_from_gal_<int:gal_id>')
def del_img_from_gal(img_id, gal_id):
    gal = Gallery.query.get(gal_id)
    img = Image.query.get(img_id)
    gal.rm_img(img)
    return '', 201


@admin.route('/reorder_<int:gal_id>', methods=['POST'])
def gal_reorder(gal_id):
    '''
        Change image ordering in gallery using ajax.
        javascript func reorder(gal_id) code in admin/image/gallery_update
    '''
    gal = Gallery.query.get(gal_id)
    for img in gal.images:
        gal.images.remove(img)
    
    data = request.get_json()
    list_ids = data.get('data')
    order_num = 1
    for id in list_ids:
        # insert img to gallery in database
        img = Image.query.get(int(id))
        print('img id: ', img.id)
        print('order num: ', order_num)
        gal.images.append(img)
        
        # update order in database
        stmt = (
            update(gallery_images).
            where(gallery_images.c.gallery_id == gal_id).
            where(gallery_images.c.image_id == img.id).
            values(img_order=order_num)
            )
        db.session.execute(stmt)
        order_num +=1
    
    db.session.commit()
    return '', 201


@admin.route('/change_data', methods=['POST'])
def change_data():
    '''
        Change data of gallery or image objects using ajax post method
        javascript func change_data(data) code in admin/image/gallery_update
    '''
    data = request.get_json()
    obj = data['data'].get('obj')
    
    if obj == 'gallery':
        obj = Gallery.query.get(data['data'].get('id'))
    elif obj == 'image':
        obj = Image.query.get(data['data'].get('id'))

    if 'title' in data['data']['change']:
        obj.title = data['data']['change']['title']
    if 'alt' in data['data']['change']:
        obj.alt = data['data']['change']['alt']
    
    db.session.commit()
    return '',201