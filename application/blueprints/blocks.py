from flask import Blueprint


block = Blueprint('block', __name__,
                        template_folder='templates')

from ..views.blocks.admin import *
