from flask import render_template
from flask import Blueprint

contact = Blueprint('contact', __name__)

@contact.route("/contact")
def Contact():
    return render_template('contact.html', title='Contact')