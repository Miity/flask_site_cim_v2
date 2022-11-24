import os
from application import db, app
from application.models.image import Image, Gallery
from werkzeug.utils import secure_filename
from flask import send_from_directory, request


@app.route('/img/<path:dir>/<path:title>/<int:id>', methods=['GET']) 
def get_image(id,title):
    image:Image = Image.query.get(id)
    return send_from_directory(app.config['UPLOAD_FOLDER'], os.path.join(image.folder,image.title))



def allowed_file(filename): 
    return '.' in filename and\
        filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def new_image(file, alt:str=None, folder:str='default') -> Image:
    if file and allowed_file(file.filename):
        img:Image = Image()
        img.title = secure_filename(file.filename)
        img.folder = folder
        file.save(img.upload_path())
        if alt:
            img.alt = alt
        else:
            img.alt = file.filename.strip('.')[0]
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
    