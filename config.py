import os


class Config:
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or '\x9c\xd5\x8f\x045\xe4D\xa1k\x99\xb3U+@G\xd7XM\x0e]\x1e\x8fj\xbe'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    # Database Options
    dbhost = 'daazdb'
    db = 'daaz_dev'
    dbuser = 'daazuser'
    dbpass = 'daaz'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DAAZDB-DEV') or 'mysql://' + dbuser + ':' + dbpass + '@' + dbhost + '/' + db
    # Mail Options
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # Uploading File Options
    UPLOAD_FOLDER = '/tmp'
    GITHUB_BASE_URL = 'https://api.github.com/'
    GITHUB_AUTH_URL = 'https://github.com/login/oauth/'
    GITHUB_CLIENT_ID = 'XXX'
    GITHUB_CLIENT_SECRET = 'YYY'


class TestingConfig(Config):
    TESTING = True
    dbhost = 'daazdb'
    db = 'daaztest'
    dbuser = 'daazuser'
    dbpass = 'd44z'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DAAZDB-TEST') or 'mysql://' + dbuser + ':' + dbpass + '@' + dbhost + '/' + db



class ProductionConfig(Config):
    TESTING = True
    dbhost = 'daazdb'
    db = 'daaz-prod'
    dbuser = 'daazuser'
    dbpass = 'd44z'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DAAZDB-PROD') or 'mysql://' + dbuser + ':' + dbpass + '@' + dbhost + '/' + db
    # Mail Options
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # Uploading File Options
    UPLOAD_FOLDER = '/tmp'
    GITHUB_BASE_URL = 'https://api.github.com/'
    GITHUB_AUTH_URL = 'https://github.com/login/oauth/'

# Will be imported in the factory fn
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig}
