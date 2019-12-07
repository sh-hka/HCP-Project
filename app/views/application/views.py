from app.views.application import Application

from flask import Blueprint, render_template

# Create a blueprint for the application
applybp = Blueprint("applybp", __name__, url_prefix='/apply')
