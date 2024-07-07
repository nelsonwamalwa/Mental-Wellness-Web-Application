from flask import render_template
from flask import Blueprint

about = Blueprint('about', __name__)

@about.route("/about")
def About():
    return render_template('about.html', title='About')