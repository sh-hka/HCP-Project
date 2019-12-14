from flask import Flask

app = Flask(__name__)

# Setup the app with the config.py file
app.config.from_object("app.config")

# Setup the logger
from app.logger_setup import logger

# Setup the password crypting
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

# Setup the database
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

from app.provider import Provider
from app.application import Application

# Setup the mail server
from flask_mail import Mail

mail = Mail(app)

# Setup the debug toolbar
from flask_debugtoolbar import DebugToolbarExtension

app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
app.config['DEBUG_TB_PROFILER_ENABLED'] = True
toolbar = DebugToolbarExtension(app)

# Import the views
from app.views import main, error

from app.views.search import searchbp
from app.application import applybp

for bp in [searchbp, applybp]:
    app.register_blueprint(bp)


from app import admin
