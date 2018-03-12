import os

from flask import Blueprint, request, current_app
from flask_restful import Api, Resource

from ..common.failures import Failures
from ..exceptions import ApiException

from .schema import VintageSchema


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

        if int(vintage_id) == 42069:
            with open(os.path.dirname(os.path.abspath(__file__)) +
                      '/testing/42069.json'.format(vintage_id),
                      'rb') as jsonfile:
                vintages_json = jsonfile.read().decode("utf-8")

            schema = VintageSchema()

            response, response_errors = schema.loads(vintages_json)
            return response

        """
        with open(os.path.dirname(os.path.abspath(__file__)) +
                  '/json/{0}.json'.format(vintage_id), 'rb') as jsonfile:
            vintages_json = jsonfile.read().decode("utf-8")

        schema = VintageSchema()

        response, response_errors = schema.loads(vintages_json)

        return response
        """
