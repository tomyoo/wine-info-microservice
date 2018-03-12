from ..exceptions import ApiException

from ...extensions import db
from ...models.wines import Wine


def get_wine_by_id(wine_id):
    try:
        wine = Wine.query.filter(db.and_(Wine.id == wine_id)).first()
    except AttributeError:
        raise ApiException("No wine with that ID found.")

    return wine
