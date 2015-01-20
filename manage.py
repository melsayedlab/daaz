#!/usr/bin/env python
from app import factory_fn
from flask.ext.script import Manager, Shell
from app.models import Users


app = factory_fn('default')
manager = Manager(app)

def make_shell_context():
    return dict(app=app, Users=Users)

manager.add_command("shell", Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
