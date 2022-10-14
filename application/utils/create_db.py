from app import db
from models.page import Page
from models.user import User
from models.block import Block
from models.image import Image, Gallery
from models.text import Text


def drop_creat_db(db):
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    drop_creat_db(db)