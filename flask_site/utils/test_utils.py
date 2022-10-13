import os
from app import app, db
from models.page import Page
from models.user import User
from models.block import Block
from models.image import Image, Gallery

#new table
def new_db():
    import flask_site.utils.create_db as create_db

def add_img_in_gallery():
    img1 = Image.query.get(1)
    img2 = Image.query.get(2)
    img3 = Image.query.get(3)
    img4 = Image.query.get(4)
    gal = Gallery()
    gal.images.append(img1)
    gal.images.append(img2)
    gal.images.append(img3)
    gal.images.append(img4)
    db.session.add(gal)
    db.session.commit()

def remove_img_from_gallery():
    image = Image.query.get(1)
    gal = Gallery.query.get(1)
    if image in gal.images:
        gal.rm_img(image)

def import_img():
    importDir = 'utils/import/'
    saveDir = os.path.join(app.config['UPLOAD_FOLDER'], 'import/')
    for file in os.listdir(importDir):
        try:
            with open(importDir+file,'rb',) as f:

                f_name = f.name.split('/')[-1]
                if f.name.split('.')[-1] in ('jpg','png','jpeg','JPG','PNG'):
                    with open(saveDir+f_name, 'wb') as nf:
                        nf.write(f.read())
                        nf.close

                        new_image = Image(title=f_name, folder='import/')
                        db.session.add(new_image)
                        db.session.commit()
                    f.close
        except OSError as er:
            print('erorre')
            print(er)

def add_block():
    block = Block()
    db.session.add(block)
    db.session.commit()

def add_image_block():
    image = Image.query.get(1)
    block = Block.query.get(1)
    image.blocks.append(block)
    db.session.commit()

def add_gallery_block():
    gallery = Gallery.query.get(1)
    block = Block()
    block.gallery = gallery
    db.session.add(block)
    db.session.commit()

def select_gallery_block():
    block = Block.query.get(1)
    print(block.image)
    gallery = Gallery.query.get(1)
    print(gallery.blocks[0])

def creat_page():
    page = Page()
    db.session.add(page)
    db.session.commit()

def add_block_to_page():
    page = Page.query.get(1)
    block = Block.query.get(1)
    block.page = page
    db.session.commit()

def select_block_in_page():
    page = Page.query.get(1)
    print(page.blocks)
    print(page.blocks[0].order)
    print(page.blocks[0].type())
    print(page.blocks[0].image.title)

def show_blocks():
    page = Page.query.get(2)
    blocks = page.blocks
    print(blocks)
    for block in blocks:
        print(block.type())







# new_db()
# import_img()
add_img_in_gallery()
#remove_img_from_gallery()
#add_block()
#add_image_block()
#add_gallery_block()
#select_gallery_block()
#creat_page()
#add_block_to_page()
#select_block_in_page()
#show_blocks()
