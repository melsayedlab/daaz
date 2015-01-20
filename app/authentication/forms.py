from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required, Email, Length


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Email(), Length(1,64)])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Remember Me')
    login = SubmitField("Login")
