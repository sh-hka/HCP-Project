from google.cloud import language_v1
from google.cloud.language_v1 import enums

from geocoder import google as google_geocode

from app.provider import Provider

ENTITY_TYPE = enums.Entity.Type

EXCLUDE_ENTITY_TYPES = {ENTITY_TYPE.PHONE_NUMBER, ENTITY_TYPE.ADDRESS, ENTITY_TYPE.LOCATION, ENTITY_TYPE.NUMBER,
                        ENTITY_TYPE.DATE, ENTITY_TYPE.EVENT, ENTITY_TYPE.PRICE}


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

    def search(self, provider: Provider.__class__):
        query = provider.query
        if self.parsed_query['address'] is not None:
            # Address - single address/area
            pass
        elif len(self.parsed_query['locations']) > 0:
            # Locations - Union of locations
            for location in self.parsed_query['locations']:
                pass
        else: # IE. Query string didn't yield any location based filter
            pass

        for string in self.parsed_query['strings']:
            pass
        matches: Provider = query.limit(30).all()
        return [match.to_dict() for match in matches]

    @staticmethod
    def __parse_query(query):
        type_ = enums.Document.Type.PLAIN_TEXT
        document = {'content': query, 'type': type_}
        encoding_type = enums.EncodingType.UTF8

        nlp_entities = SearchQuery.NLP_CLIENT.analyze_entities(document, encoding_type=encoding_type).entities

        address_entity = [e.name for e in nlp_entities if e.type == ENTITY_TYPE.ADDRESS]
        address_geocode = google_geocode(address_entity[0]) if len(address_entity) > 0 else None
        address = None
        if address_geocode is not None and address_geocode.ok:
            address = address_geocode.current_result
        location_entities = [e.name for e in nlp_entities if e.type == ENTITY_TYPE.LOCATION]
        locations = []
        if address is None and len(location_entities) > 0:
            locations_geocode = [google_geocode(loc) for loc in location_entities]
            locations = [loc.current_result for loc in locations_geocode if loc.ok]
        other_entities = [e.name for e in nlp_entities if e.type not in EXCLUDE_ENTITY_TYPES]

        parsed_query = {
            'address': address,
            'locations': locations,
            'strings': other_entities
        }
        return parsed_query
