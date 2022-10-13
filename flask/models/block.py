from app import db
from sqlalchemy import func 


class Block(db.Model):
    __tablename__ = 'blocks'

    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Integer)

    page_id = db.Column(db.Integer, db.ForeignKey('page.id'))
    page = db.relationship("Page", back_populates="blocks")

    text_id = db.Column(db.Integer, db.ForeignKey('text.id'))
    text = db.relationship("Text", back_populates="blocks", cascade="all,delete")

    gallery_id = db.Column(db.Integer, db.ForeignKey("gallery.id"))
    gallery = db.relationship("Gallery", back_populates="blocks", cascade="all,delete")
    
    image_id = db.Column(db.Integer, db.ForeignKey("image.id"))
    image =  db.relationship("Image", back_populates="blocks", cascade="all,delete")

    def __init__(self, **kwargs):
        max_order_row = db.session.query(func.max(Block.order)).first()[0]
        if max_order_row != None:
            kwargs['order'] = max_order_row + 1
        else:
            kwargs['order'] = 1
        super(Block, self).__init__(**kwargs)

    def __repr__(self):
        return '<Block: {}>'.format(self.id)

    def type(self):
        if self.text:
            return 'text'
        elif self.gallery:
            return 'gallery'
        elif self.image:
            return 'image'
        elif self.card:
            return 'card'
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
