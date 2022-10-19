from application.blocks import block
from application.app import db
from application.models.block import Block
from flask import request, render_template, jsonify
from application.models.text import Text
from application.models.image import Image, Gallery
from application.models.page import Page
import json


@block.route('/block_add', methods=['Post'])
def block_add():
    data = request.get_json()
    block = Block()
    block.page = Page.query.get(int(data['data'].get('page_id')))
    db.session.add(block)

    data = chose_block_template(block, data['data'].get('type'))
    return jsonify(data)

@block.route('/block_update', methods=['Post'])
def block_update():
    data = request.get_json()

    if data.get('type') == 'reorder': 
        block_ids = data.get('block_ids')
        order = 1
        for id in block_ids:
            block = Block.query.get(int(id))
            block.order = order
            db.session.commit()
            order +=1

    if data.get('type') == 'remove':
        id = data.get('block_id')
        block = Block.query.get(int(id))
        block.delete()

    if data.get('type') == 'text':
        text = Text.query.get((data.get('id')))
        text.text = data.get('value')
        db.session.commit()

    return ('', 204)


@block.route('/uploadFiles', methods=['Post'])
def uploadFiles():
    '''
        send formData by ajax for update image 
        where: admin/page/page_add
    '''
    
    data = json.loads(request.form.get('data'))
    files = request.files
    if data['type'] == 'image': 
        img = Image.query.get(int(data['id']))
        img.update(new_file=files['file0'])

    elif data['type'] == 'gallery':
        gal = Gallery.query.get(int(data['id']))
        for file in files:

            img = Image()
            db.session.add(img)
            print(files[file])
            print(files[file].filename)
            img.update(new_file=files[file])
            gal.add_img(img)

    return ('', 204)


def chose_block_template(block, type):
    if type == 'text':
        text = Text()
        db.session.add(text)
        block.text = text
        db.session.commit()
        template = render_template('admin/block/inp_text.html', text=text, block=block)

    elif type == 'image':
        image = Image()
        db.session.add(image)
        block.image = image
        db.session.commit()
        template = render_template('admin/block/image.html', image=image, block=block)
    
    elif type == 'gallery':
        gal = Gallery()
        db.session.add(gal)
        block.gallery = gal
        db.session.commit()
        template = render_template('admin/block/gallery.html', gallery = gal, block = block)

    return {'template':template,'block_id':block.id}