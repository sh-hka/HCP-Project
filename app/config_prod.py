import logging
from os import environ

from app.config_common import *


# DEBUG has to be to False in a production environment for security reasons
DEBUG = False

# Secret key for generating tokens
SECRET_KEY = 'houdini'

# Google Maps API key
GOOGLE_MAPS_API_KEY = environ['GOOGLE_MAPS_API_KEY']

# Admin credentials
ADMIN_CREDENTIALS = (environ['HCP_ADMIN'], environ['HCP_PASS'])

# Database choice
SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Configuration of a Gmail account for sending mails
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'flask.boilerplate'
MAIL_PASSWORD = 'flaskboilerplate123'
ADMINS = ['flask.boilerplate@gmail.com']

# Number of times a password is hashed
BCRYPT_LOG_ROUNDS = 12

LOG_LEVEL = logging.INFO
LOG_FILENAME = 'activity.log'
LOG_MAXBYTES = 1024
LOG_BACKUPS = 2
