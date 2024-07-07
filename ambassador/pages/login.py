from flask_login import login_user, current_user
from flask import render_template, url_for, flash, redirect, request
from ambassador.forms import LoginForm
from ambassador.models import User
from ambassador import bcrypt
from flask import Blueprint

login = Blueprint('login', __name__)

@login.route("/login", methods=['GET', 'POST'])
def Login():
    if current_user.is_authenticated:
        return redirect(url_for('blog'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('blog.Blog'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
