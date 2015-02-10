from flask import render_template, redirect, url_for, flash
from flask.ext.login import login_user, logout_user, login_required, current_user
from ..email import send_mail
from . import authentication
from .forms import LoginForm, SignupForm
from .. import daazdb
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


@authentication.route('/signup', methods=['GET', 'POST'])
def signup():
    signupform = SignupForm()
    if signupform.validate_on_submit():
        # Add This User To The Database
        newuser = Users()
        newuser.email = signupform.email.data
        newuser.name = signupform.username.data
        newuser.password = signupform.password.data
        daazdb.session.add(newuser)
        daazdb.session.commit()
        confirm_token = newuser.create_token()
        send_mail(newuser.email, 'Confirmation Email', 'authentication/email/confirm', newuser=newuser, confirm_token=confirm_token)
        flash('Confirmation email has been sent !.')
        return redirect(url_for('main.index'))
    return render_template('authentication/signup.html', signupform=signupform)

@authentication.route('/confirm/<token>')
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash("You have successfully activated your account.")
    else:
        flash("The link is invalid or expired, please try to sign up again.")
    return redirect(url_for('main.index'))
