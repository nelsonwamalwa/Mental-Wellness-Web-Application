from flask import render_template
from flask import Blueprint

article = Blueprint('article', __name__)

@article.route("/article")
def Article():
    return render_template('article.html', title='Article')