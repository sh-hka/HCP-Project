from flask import render_template
from app import app
from app.views.search import SearchForm


@app.route('/')
@app.route('/index')
def index():
    form = SearchForm()
    return render_template('index.html', form=form, title='Home')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')
