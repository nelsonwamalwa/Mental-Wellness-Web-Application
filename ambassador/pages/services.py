from flask import render_template
from flask import Blueprint

services = Blueprint('services', __name__)

@services.route("/services")
def Services():
    return render_template('services.html', title='Services')