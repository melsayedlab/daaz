from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
from flask.ext.login import LoginManager
from flask.ext.github import GitHub
from config import config

manager = Manager()
bootstrap = Bootstrap()
daazdb = SQLAlchemy()
mail = Mail()
github = GitHub()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'authentication.login'


def factory_fn(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    daazdb.init_app(app)
    login_manager.init_app(app)
    github.init_app(app)

    # routes here - register with blueprint
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from authentication import authentication as login_auth
    app.register_blueprint(login_auth)

    return app
