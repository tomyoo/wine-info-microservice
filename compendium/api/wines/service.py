from ..exceptions import ApiException

from ...extensions import db
from ...models.wines import Wine
from ...models.vintages import Vintage


def get_wine_by_id(wine_id):
    try:
        wine = Wine.query.filter(db.and_(Wine.id == wine_id)).first()
    except AttributeError:
        raise ApiException("No wine with that ID found.")

    return wine


def get_vintage_by_id(vintage_id):
    try:
        vintage = Vintage.query.filter(db.and_(
            Vintage.id == vintage_id)).first()
    except AttributeError:
        raise ApiException("No vintage with that ID found.")

    return vintage
