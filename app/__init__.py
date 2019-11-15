from app import admin
from app.models import User
from flask_login import LoginManager
from app.views import main, user, error
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from app.logger_setup import logger
from flask import Flask

app = Flask(__name__)

# Setup the app with the config.py file
app.config.from_object("app.config")

# Setup the logger

# Setup the database
db = SQLAlchemy(app)

# Setup the mail server
mail = Mail(app)

# Setup the debug toolbar
app.config["DEBUG_TB_TEMPLATE_EDITOR_ENABLED"] = True
app.config["DEBUG_TB_PROFILER_ENABLED"] = True
toolbar = DebugToolbarExtension(app)

# Setup the password crypting
bcrypt = Bcrypt(app)

# Import the views
app.register_blueprint(user.userbp)

# Setup the user login process

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "userbp.signin"


@login_manager.user_loader
def load_user(email):
    return User.query.filter(User.email == email).first()
