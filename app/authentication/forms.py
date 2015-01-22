from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required, Email, Length, EqualTo
from ..models import Users
from wtforms import ValidationError


class LoginForm(Form):
    email = StringField(
        'Email', validators=[Required(), Email(), Length(1, 64)])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Remember Me')
    login = SubmitField("Login")


class SignupForm(Form):
    username = StringField('Username', validators=[Required()])
    email = StringField(
        'Email', validators=[Required(), Email(), Length(1, 64)])
    password = PasswordField('Password', validators=[Required(), EqualTo(
        'password_confirm', message='Please Match The Passwords')])
    password_confirm = PasswordField(
        'Confirm Password', validators=[Required()])
    register = SubmitField("Sign Up")

    def validate_email(self, emailf):
        if Users.query.filter_by(email=emailf.data).first():
            raise ValidationError('Email Address Already Exist.')

    def validate_username(self, unamef):
        if Users.query.filter_by(name=unamef.data).first():
            raise ValidationError('Username Already Exist.')
