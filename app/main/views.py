from flask import Flask, session, url_for, flash, render_template
from . import main
from .forms import LoginForm
from .. import daazdb
from ..models import Users

@main.route('/', methods=['GET', 'POST'])
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