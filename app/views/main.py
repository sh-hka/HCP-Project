from flask import render_template, jsonify
from app import app
from app.forms import search as search_form


@app.route('/')
@app.route('/index')
def index():
    form = search_form.Search()
    return render_template('index.html', form=form, title='Home')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')


@app.route('/search', methods=['GET'])
def search():
    return render_template('layout.html', title='Results')


@app.route('/search', methods=['POST'])
def results():
    return jsonify({})
