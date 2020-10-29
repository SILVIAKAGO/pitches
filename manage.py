from app import create_app,db
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand
from app.models import User,Category,Pitch,Comments,Votes

app = create_app('production')
# app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Category=Category, Pitch=Pitch, Comments=Comments, Votes=Votes)
if __name__ == '__main__':
    manager.run()