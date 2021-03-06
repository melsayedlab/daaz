from . import daazdb
from . import login_manager
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from . import daazdb

# a callback function which will be used with the extenstion


@login_manager.user_loader
def load_user(id):
    # this function return the user object if found
    # and None if not, required by the ext
    return Users.query.get(int(id))


class Users(UserMixin, daazdb.Model):
    __tablename__ = 'users'
    id = daazdb.Column(daazdb.Integer, primary_key=True)
    email = daazdb.Column(daazdb.String(64), unique=True)
    name = daazdb.Column(daazdb.String(64), unique=True)
    pass_hash = daazdb.Column(daazdb.String(128))
    confirmed = daazdb.Column(daazdb.Boolean,default=False)

    def create_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})


    def confirm(self, confirm_token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data_id = s.loads(confirm_token)
        except:
            return False
        if data_id.get('confirm') != self.id:
            return False
        else:
            self.confirmed = True
            daazdb.session.add(self)
            return True
    @property
    def password(self):
        raise AttributeError('password is a write only attribute')

    @password.setter
    def password(self, password):
        self.pass_hash = generate_password_hash(password)

    def verify_pass(self, password):
        return check_password_hash(self.pass_hash, password)
