from application.app import db


def drop_creat_db(db):
    from application.models.page import Page
    from application.models.user import User
    from application.models.block import Block
    from application.models.image import Image, Gallery
    from application.models.text import Text
    db.drop_all()
    db.create_all()
    
drop_creat_db(db)