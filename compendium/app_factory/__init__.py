from flask import Flask

from .configure_logging import configure_logging
from .initialize_extensions import initialize_extensions
from .register_blueprints import register_blueprints
from ..extensions import schemas, db, statsd


def create_app(package_name, package_path, settings_override=None,
               extensions=None, env='dev'):
    """Returns a :class:`Flask` application instance configured with common
    functionality for this application.

    :param package_name: application package name
    :param package_path: application package path
    :param settings_override: a dictionary or path to file of settings to
        override
    :param extensions: an array of instances of additional extensions to
        initialize on the app
    """
    app = Flask(package_name)
    # Load environment specific configuration
    app.config.from_pyfile('config/%s.py' % env)

    if isinstance(settings_override, str):
        app.config.from_pyfile(settings_override, silent=True)
    else:
        app.config.from_object(settings_override)

    register_blueprints(app, package_name, package_path)
    common_extensions = frozenset([schemas, db, statsd])

    initialize_extensions(app, common_extensions)
    initialize_extensions(app, extensions)

    return app
