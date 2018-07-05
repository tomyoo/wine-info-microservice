from ..exceptions import ApiException

from ...extensions import db
from ...models.vintages import Vintage, Region, Grape


def get_vintage_by_id(vintage_id):
    try:
        vintage = Vintage.query.filter(db.and_(
            Vintage.id == vintage_id)).first()
    except AttributeError:
        raise ApiException("No vintage with that ID found.")

    return vintage


def get_region_by_id(region_id):
    try:
        region = Region.query.filter(db.and_(
            Region.id == region_id)).first()
    except AttributeError:
        raise ApiException("No region with that ID found.")

    return region
