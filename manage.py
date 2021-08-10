# flask related importation
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


## project level importation
from app import create_app, db

##Standard Python modules importation
import os
import sys


app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():

    return dict(app = app, db = db)


@manager.command
def test():

    pass 

@manager.command
def deploy():

    pass

manager.add_command("shell", Shell(make_context = make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':

	manager.run()