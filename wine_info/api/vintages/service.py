from ..exceptions import ApiException

from ...extensions import db
from ...models.vintages import Vintage


def get_vintage_by_id(vintage_id):
    try:
        vintage = Vintage.query.filter(db.and_(
            Vintage.id == vintage_id)).first()
    except AttributeError:
        raise ApiException("No vintage with that ID found.")

    return vintage
