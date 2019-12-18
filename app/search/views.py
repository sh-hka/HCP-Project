from flask import Blueprint, render_template, jsonify

# Create a search blueprint
searchbp = Blueprint("searchbp", __name__)


@searchbp.route('/search', methods=["GET"])
def search():
    return render_template('layout.html', title='Results')


@searchbp.route('/search', methods=['POST'])
def results():
    return jsonify([{}])
