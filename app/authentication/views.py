from flask import render_template, redirect, url_for, flash
from flask.ext.login import login_user, logout_user, login_required
from . import authentication
from .forms import LoginForm
from ..models import Users


@authentication.route('/login', methods=['GET', 'POST'])
def login():
    loginform = LoginForm()
    if loginform.validate_on_submit():
        # check if the user's email in the database
        user = Users.query.filter_by(email=loginform.email.data).first()
        if user is not None and user.verify_pass(loginform.password.data):
            login_user(user, loginform.remember_me.data)
            return redirect(url_for('main.index'))
        flash('Invalid Email Or Password')
    return render_template('authentication/login.html', loginform=loginform)


@authentication.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logged out')
    return redirect(url_for('main.index'))
