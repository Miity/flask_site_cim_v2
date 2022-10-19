from application.app import db
from application.models.block import Block


class Page(db.Model):
    __tablename__ = 'page'

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(255), unique=True)
    title = db.Column(db.String(80), nullable=True, unique=True)
    description = db.Column(db.String(250), nullable=True)
    archive = db.Column(db.Boolean)

    blocks = db.relationship('Block', back_populates='page', cascade="all,delete" , order_by = Block.order)

    def __init__(self, **kwargs):
        kwargs['archive'] = True
        super(Page, self).__init__(**kwargs)

    def __repr__(self):
        return '<Page %r>' % (self.title)

    def delete(self):
        if self.archive == False:
            self.archive = True
            db.session.commit()
        elif self.archive == True:
            db.session.delete(self)
            db.session.commit()
