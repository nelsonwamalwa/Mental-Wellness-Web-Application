from flask import render_template, url_for, flash, redirect
from flask_login import current_user
from ambassador import db, bcrypt
from ambassador.forms import RegistrationForm
from ambassador.models import User
from flask import Blueprint

register = Blueprint('register', __name__)

@register.route("/register", methods=['GET', 'POST'])
def Register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login.Login'))
    return render_template('register.html', title='Register', form=form)
