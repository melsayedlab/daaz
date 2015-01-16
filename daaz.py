from flask import Flask, render_template, session, url_for, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager, Shell
from flask.ext.wtf import Form
from flask.ext.sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
daazdb = SQLAlchemy(app)


class Users(daazdb.Model):
    __tablename__ = 'users'
    id = daazdb.Column(daazdb.Integer, primary_key=True)
    name = daazdb.Column(daazdb.String(32), unique=True)
    password = daazdb.Column(daazdb.String(32), unique=True) #MD5 Hashed

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://daazuser:d44z@daazdb/daaz'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SECRET_KEY'] = '\x9c\xd5\x8f\x045\xe4D\xa1k\x99\xb3U+@G\xd7XM\x0e]\x1e\x8fj\xbe'

class LoginForm(Form):
    username = StringField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    login = SubmitField("Login")


@app.route('/', methods=['GET', 'POST'])
def index():
    loginform = LoginForm()
    if loginform.validate_on_submit():
        #check if the user in the database
        user = Users.query.filter_by(name=loginform.username.data).first()
        #check the password
        password = Users.query.filter_by(password=loginform.password.data).first()
        if user is None or password is None:
            flash('username or password not correct!')
    return render_template('index.html', loginform=loginform)

if __name__ == '__main__':
    manager.run()
