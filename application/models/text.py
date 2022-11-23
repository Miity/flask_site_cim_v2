from application import db


class Text(db.Model):
    __tablename__ = 'text'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=True)

    blocks = db.relationship('Block', back_populates='text', cascade="all,delete")
    

    def __repr__(self):
        return f'<Text id: {self.id}>'