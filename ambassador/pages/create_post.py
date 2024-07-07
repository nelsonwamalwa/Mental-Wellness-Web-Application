from flask import render_template
from flask import Blueprint

create_post = Blueprint('create_post', __name__)

@create_post.route("/create_post")
def Create_post():
    return render_template('create_post.html', title='Create_post')