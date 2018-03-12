from flask_script import (Manager, Server)
from wine_info.api import create_app


manager = Manager(create_app)


manager.add_command('runserver', Server())


if __name__ == '__main__':
    manager.run()
