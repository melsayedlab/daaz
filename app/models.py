from . import daazdb
class Users(daazdb.Model):
    __tablename__ = 'users'
    id = daazdb.Column(daazdb.Integer, primary_key=True)
    name = daazdb.Column(daazdb.String(32), unique=True)
    password = daazdb.Column(daazdb.String(32), unique=True) #MD5 Hashed
    @property
    def password(self):
        raise AttributeError('password is a write only attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)