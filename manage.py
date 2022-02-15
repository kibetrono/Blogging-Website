from app import create_app, db
from flask_script import Manager, Server
from app.models import User,Post,Role,Comment
from  flask_migrate import Migrate, MigrateCommand


if __name__ == '__main__':
    manager.run()
