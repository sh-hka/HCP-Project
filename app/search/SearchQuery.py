from google.cloud import language_v1
from google.cloud.language_v1 import enums


class BadQueryException(Exception):
    def __init__(self, msg=None):
        self._msg = msg
        super(Exception, msg)

    def get_msg(self):
        return self._msg


class SearchQuery:

    NLP_CLIENT = language_v1.LanguageServiceClient()

    def __init__(self, query: str = None, position: dict = None, search_range=None):
        self.query = query
        self.position = position
        self.range = search_range
        if query is None or query == '':
            if position is None:
                raise BadQueryException("Empty SearchQuery not permitted")
            elif position.keys() != {'lat', 'lng'}:
                raise BadQueryException("Malformed SearchQuery")
            self.position = position
        else:
            self.parsed_query = self.__parse_query(query)

    @staticmethod
    def __parse_query(query):
        type_ = enums.Document.Type.PLAIN_TEXT
        document = {'content': query, 'type': type_}
        encoding_type = enums.EncodingType.UTF8

        nlp_response = SearchQuery.NLP_CLIENT.analyze_entities(document, encoding_type=encoding_type)

        # TODO: See the response and generate a dict of all the important stuff

        parsed_query = {
            'locale': {'state': None, 'city': None, 'zip': None},
        }
        return parsed_query
