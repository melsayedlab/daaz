#!/usr/bin/env python
from app import factory_fn
from flask.ext.script import Manager, Shell
from app.models import Users
from flask.ext.migrate import Migrate, MigrateCommand
from app import daazdb

app = factory_fn('default')
manager = Manager(app)
migrate = Migrate(app,daazdb)

def make_shell_context():
    return dict(app=app, daazdb=daazdb, Users=Users)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
