from compendium.extensions import schemas, statsd
#from .logging import setup_logging
from .handlers import setup_handlers
from ..app_factory import create_app as factory_create_app


def create_app(settings_override=None, env='dev'):
    """Returns an api application instance"""
    extensions = frozenset([statsd, schemas])

    app = factory_create_app(__name__, __path__, settings_override, extensions,
                             env=env)

    if not app.extensions:
        app.extensions = {}
    app.extensions['statsd'] = statsd

    # Load environment specific configuration
    app.config.from_pyfile('config/%s.py' % env)

    #setup_logging(app)
    setup_handlers(app)

    return app
