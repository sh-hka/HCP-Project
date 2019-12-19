from app.search.SearchQuery import (
    SearchQuery,
    BadQueryException,
)

from flask import (
    Blueprint,
    render_template,
    jsonify,
    request,
)

from flask_api import status
from urllib.parse import unquote

import json

# Create a search blueprint
searchbp = Blueprint("searchbp", __name__)


@searchbp.route('/search', methods=["GET"])
def search():
    return render_template('layout.html', title='Results')


@searchbp.route('/search', methods=['POST'])
def results():
    query_data: dict = request.json
    if query_data is None:
        return jsonify([{}])
    query = query_data.get('query', None)
    position = query_data.get('position', None)
    search_range = query_data.get('range', None)
    try:
        search_query = SearchQuery(
            query=query,
            position=position,
            search_range=search_range
        )
    except BadQueryException as e:
        response = jsonify(error=e.get_msg()), status.HTTP_400_BAD_REQUEST
        return response
    return jsonify([{}])
