import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///data/test.db'
    SECRET_KEY = 'qazzaq'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    STATIC_FOLDER = os.path.join(PROJECT_DIR, 'static')
    MEDIA_FOLDER = os.path.join(STATIC_FOLDER, 'media')
    UPLOAD_FOLDER = os.path.join(MEDIA_FOLDER, 'upload')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024