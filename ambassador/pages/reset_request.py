from flask import Blueprint, render_template, redirect, url_for, flash, request
from ambassador import db, mail
from ambassador.models import User
from flask_login import current_user
from itsdangerous import URLSafeTimedSerializer
from flask import current_app as app
from ambassador.pages import reset_request  # Import RequestResetForm

reset_request = Blueprint('reset_request', __name__)

@reset_request.route('/reset_password', methods=['GET', 'POST'])
def Reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))  # Redirect to the main page or a relevant page for authenticated users

    form = reset_request()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            # Generate reset token
            token = user.get_reset_token()

            # Send reset email
            send_reset_email(user, token)

            flash('An email has been sent with instructions to reset your password.', 'info')
            return redirect(url_for('login.Login'))

        flash('Email address not found. Please check and try again.', 'danger')

    return render_template('reset_request.html', title='Reset Password', form=form)

def send_reset_email(user, token):
    # Create the reset password link
    reset_link = url_for('reset_token.Reset_token', token=token, _external=True)

    # Compose email message
    subject = "Reset Your Password"
    body = f"To reset your password, click the link below:\n{reset_link}"

    # Send email
    mail.send_message(
        subject,
        recipients=[user.email],
        body=body
    )
