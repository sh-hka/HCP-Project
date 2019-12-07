from flask import Flask

app = Flask(__name__)

# Setup the app with the config.py file
app.config.from_object("app.config")

# Setup the logger
from app.logger_setup import logger

# Setup the database
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

# Setup the mail server
from flask_mail import Mail

mail = Mail(app)

# Setup the debug toolbar
from flask_debugtoolbar import DebugToolbarExtension

app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
app.config['DEBUG_TB_PROFILER_ENABLED'] = True
toolbar = DebugToolbarExtension(app)

# Setup the password crypting
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

# Import the views
from app.views import main, user, error

app.register_blueprint(user.userbp)

from app.views.search import searchbp
from app.views.application import applybp

for bp in [searchbp, applybp]:
    app.register_blueprint(bp)

# Setup the user login process
from flask_login import LoginManager
from app.models import User
from app.views.application import Application

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "userbp.signin"


@login_manager.user_loader
def load_user(email):
    return User.query.filter(User.email == email).first()


from app import admin
