from flask import Blueprint, render_template, redirect, url_for, flash
from ambassador.forms import ResetPasswordForm
from ambassador.models import User
from flask_login import login_user
from werkzeug.security import generate_password_hash
from ambassador import db

reset_token = Blueprint('reset_token', __name__)

@reset_token.route('/reset_password/<token>', methods=['GET', 'POST'])
def Reset_token(token):
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('reset_request.reset_request_view'))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        login_user(user)  # Automatically log the user in after password reset
        return redirect(url_for('login.Login'))

    return render_template('reset_password.html', title='Reset Password', form=form)
