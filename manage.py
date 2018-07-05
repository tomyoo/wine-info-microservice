from flask_script import (Manager, Server)
from flask import current_app
from compendium.api import create_app
from compendium.extensions import db
from compendium.models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


manager = Manager(create_app)
manager.add_command('runserver', Server())


@manager.command
def create_tables():
    mysql_uri = current_app.config['SQLALCHEMY_DATABASE_URI']
    engine = create_engine(mysql_uri)

    db.create_all()


if __name__ == '__main__':
    manager.run()
