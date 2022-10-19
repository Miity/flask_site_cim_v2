from flask import Blueprint


admin = Blueprint('admin', __name__,
                        template_folder='templates',
                        static_folder='static',
                        )

from .views.admin.view_page import *
from .views.admin.view_media import *
from .views.admin.view_text import *


@admin.route('/')
def index():
     return render_template('admin/index.html')