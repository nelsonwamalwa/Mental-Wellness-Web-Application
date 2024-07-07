from flask import render_template
from flask import Blueprint

layout = Blueprint('layout', __name__)

@layout.route("/layout")
def Layout():
    return render_template('layout.html', title='Layout')