from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager, Shell
from flask.ext.wtf import Form
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

manager = Manager()
bootstrap = Bootstrap()
daazdb = SQLAlchemy()

def factory_fn(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    daazdb.init_app(app)

    # routes here - register with blueprint
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
