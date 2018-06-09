import os
from dotenv import load_dotenv
import json

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

with open("settings.json", 'r') as s:
    settings = json.loads(s.read())


class Config(object):
    SECRET_KEY = settings.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = settings.get('MAIL_SERVER')
    MAIL_PORT = settings.get('MAIL_PORT') or 25
    MAIL_USE_TLS = settings.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = settings.get('MAIL_USERNAME')
    MAIL_PASSWORD = settings.get('MAIL_PASSWORD')
    ADMINS = [settings.get('ADMINS')]
    POSTS_PER_PAGE = settings.get('POSTS_PER_PAGE')
    # pages
    INDEX_URL = settings.get('INDEX_PYSHEET')
    PYSHEET_URL = settings.get('PYSHEET')
    CONTRIBUTING = settings.get('CONTRIBUTING')
