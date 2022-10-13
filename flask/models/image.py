import os
from app import db, app
from models.base import TimestampMixin
from werkzeug.utils import secure_filename
from flask import send_from_directory

gallery_images = db.Table('gallery_images',
        db.Model.metadata,
        db.Column('gallery_id', 
                db.Integer, 
                db.ForeignKey('gallery.id'), 
                primary_key=True),
        db.Column('image_id', 
                db.Integer, 
                db.ForeignKey('image.id'), 
                primary_key=True),
        db.Column('img_order',
                db.Integer,)
        )


class Image(db.Model, TimestampMixin):
    __tablename__ = 'image'

    id = db.Column(db.Integer, primary_key=True)
    folder = db.Column(db.String(80), nullable=True, default='default')
    title = db.Column(db.String(80), nullable=True)
    alt = db.Column(db.String(80), default='none')
    archive = db.Column(db.Boolean)
    
    blocks = db.relationship('Block', back_populates='image', cascade="all,delete")

    def __repr__(self):
        return f'<Image title: {self.title}>'

    def __init__(self, **kwargs):
        kwargs['archive'] = False
        super(Image, self).__init__(**kwargs)

    def upload_path(self):
        return os.path.join(app.config['UPLOAD_FOLDER'], self.folder, self.title)

    def update(self, new_file = None, data = None):
        if new_file:
            self.title = secure_filename(new_file.filename)
            db.session.commit()
            new_file.save(self.upload_path())
        elif data:
            self.title = data['title']
            self.alt = data['alt']
        db.session.commit()

    def delete(self):
        os.system("rm " + self.path_to_file())
        db.session.delete(self)
        db.session.commit()
    




class Gallery(db.Model, TimestampMixin):
    __tablename__ = 'gallery'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=True)
    
    blocks = db.relationship('Block', back_populates='gallery',cascade="all,delete")
    images = db.relationship('Image',
                secondary = gallery_images,
                lazy='subquery',
                backref=db.backref('gallery', lazy=True),
                cascade="save-update",
                order_by = gallery_images.c.img_order)

    def __repr__(self):
        return '<Gallery title: {}>'.format(self.title)
    
    def add_img(self, image):
        self.images.append(image)
        db.session.commit()
    
    def rm_img(self, image):
        self.images.remove(image)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
