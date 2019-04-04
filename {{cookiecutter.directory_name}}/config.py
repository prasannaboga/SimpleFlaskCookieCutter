import os
from os.path import join, dirname
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# For optional config variables use os.getenv('key') or os.environ.get('key')
# For mandatory config variables use os.eniron['key']

# Application
DEVELOPER_EMAIL = os.environ.get('DEVELOPER_EMAIL', None)
LOGGER_LEVEL = os.environ.get('LOGGER_LEVEL', 'INFO')
SECRET_KEY = os.environ.get('SECRET_KEY', 'SECRET_KEY')
APP_NAME = os.environ.get('APP_NAME', 'APP_NAME')

# Celery
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Mongo DB
MONGODB_HOST_URI = os.environ.get('MONGODB_HOST_URI')
MONGODB_DATABASE = os.environ.get('MONGODB_DATABASE')

# S3 bucket
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

# Mail
MAIL_SERVER = os.environ.get('MAIL_SERVER')
MAIL_PORT = os.environ.get('MAIL_PORT')
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL')
MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')

# WEBURI
WEBURI = os.environ.get('WEBURI', 'http://localhost:5000/')
