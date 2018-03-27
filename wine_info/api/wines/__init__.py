import os
import json

from flask import Blueprint, request, current_app
from flask_restful import Api, Resource

from ..common.failures import Failures
from ..exceptions import ApiException

from ...extensions import db

from .service import get_wine_by_id

from .schema import WineSchema


# named Blueprint object, so as to be registered by the app factory
blueprint = Blueprint(
    'wines', __name__, url_prefix='/wines')
api = Api(blueprint)


@api.resource('/<wine_id>')
class WineResource(Resource):

    def get(self, wine_id):
        """ Retrieve the information about a sku, like a bottle """

        if int(wine_id) == 42070:
            raise ApiException(Failures.other_error)

        elif int(wine_id) == 42069:
            with open(os.path.dirname(os.path.abspath(__file__)) +
                      '/testing/42069.json'.format(wine_id),
                      'rb') as jsonfile:
                wines_json = jsonfile.read().decode("utf-8")

            schema = WineSchema()

            response, response_errors = schema.loads(wines_json)
            return response

        else:
            wine = get_wine_by_id(wine_id)
            wine_dict = {'id': wine.id,
                         'name': wine.name,
                         'brand': wine.brand.name,
                         'variety': {
                             'name': wine.variety.name,
                             'type': wine.variety.type.value
                         },
                         'classification': {
                             'name': wine.classification.name,
                             'type': wine.classification.type.value
                         }}
            wine_json = json.dumps(wine_dict)

            schema = WineSchema()

            response, response_errors = schema.loads(wine_json)
            return response
