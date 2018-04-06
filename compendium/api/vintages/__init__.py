import os
import json

from flask import Blueprint, request, current_app
from flask_restful import Api, Resource

from ..common.failures import Failures
from ..exceptions import ApiException

from .schema import VintageSchema

from .service import get_vintage_by_id


# named Blueprint object, so as to be registered by the app factory
blueprint = Blueprint(
    'vintages', __name__, url_prefix='/vintages')
api = Api(blueprint)


@api.resource('/<vintage_id>')
class VintageResource(Resource):

    def get(self, vintage_id):
        """ Retrieve the information about a sku, like a bottle """

        if int(vintage_id) == 42070:
            raise ApiException(Failures.other_error)

        elif int(vintage_id) == 42069:
            with open(os.path.dirname(os.path.abspath(__file__)) +
                      '/testing/42069.json'.format(vintage_id),
                      'rb') as jsonfile:
                vintages_json = jsonfile.read().decode("utf-8")

            schema = VintageSchema()

            response, response_errors = schema.loads(vintages_json)
            return response


        else:

            vintage = get_vintage_by_id(vintage_id)

            wine_dict = {'id': vintage.id,
                         'year': vintage.year,
                         'short_tasting_note': vintage.short_tasting_note,
                         'tasting_note': vintage.tasting_note,
                         'abv': vintage.abv,
                         'attributes': {
                             'body': vintage.body,
                             'fruit': vintage.fruit,
                             'earth': vintage.earth,
                             'tannin': vintage.tannin,
                             'oak': vintage.oak,
                             'acidity': vintage.acidity
                         },
                         'region': [vintage.regions],
                         'grapes': [vintage.grapes],
                         'taste': [vintage.tastes],
                         'pairing': [vintage.pairings],
                         'trait': [vintage.traits],
                         'wine': {
                             'name': vintage.wine.name,
                             'brand': vintage.wine.brand.name,
                             'variety': {
                                 'name': vintage.wine.variety.name,
                                 'type': vintage.wine.variety.type.value
                             },
                             'classification': {
                                 'name': vintage.wine.classification.name,
                                 'type': vintage.wine.classification.type.value
                             }
                         }}

            wine_json = json.dumps(wine_dict)

            schema = VintageSchema()

            response, response_errors = schema.loads(wine_json)

            return response
