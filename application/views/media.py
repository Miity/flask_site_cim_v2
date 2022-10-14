import os
from app import db, app
from models.image import Image, Gallery
from werkzeug.utils import secure_filename
from flask import send_from_directory, request


@app.route('/uploads/<int:id>') 
def uploaded_image(id):
    image = Image.query.get(id)
    image_folder = os.path.join( app.config['UPLOAD_FOLDER'], image.folder)
    return send_from_directory(image_folder, image.title)



def allowed_file(filename): 
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def new_image(file, alt=None, folder='default'):
    if file and allowed_file(file.filename):
        img = Image()
        img.title = secure_filename(file.filename)
        if alt:
            img.alt = alt
        else:
            img.alt = file.filename.strip('.')[0]
        img.folder = folder
        file.save(img.upload_path())
        db.session.add(img)
        db.session.commit()
        return img

def new_gallery(title, files):
    gal = Gallery()
    gal.title = title
    
    for file in files:
        img = new_image(file,folder='gallery')
        gal.images.append(img)

    db.session.add(gal)
    db.session.commit()
    return gal