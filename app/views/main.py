from flask import render_template
from app import app
from app.views.search import SearchForm


@app.route('/')
@app.route('/index')
def index():
    form = SearchForm()
    gmaps_api_key = app.config['GOOGLE_MAPS_API_KEY']
    return render_template('index.html', form=form, title='Home', GOOGLE_MAPS_API_KEY=gmaps_api_key)


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')
