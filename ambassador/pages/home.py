from flask import render_template, Blueprint
from ambassador.models import Post
from flask import Blueprint

home = Blueprint('home', __name__)

@home.route("/")
def Home():
    posts = Post.query.filter_by(approved=True).order_by(Post.date_posted.desc()).all()
    return render_template('home.html', posts=posts)