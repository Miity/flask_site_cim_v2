import os

cur_dir = os.getcwd()
parrent_dir = os.path.abspath(os.path.join(cur_dir, os.pardir))

import sys
sys.path.append(parrent_dir)

from ..app import db
from ..models.page import Page
from ..models.user import User
from ..models.block import Block
from ..models.image import Image, Gallery
from ..models.text import Text


db.drop_all()
db.create_all()