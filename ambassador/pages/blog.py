from flask import render_template
from flask import Blueprint
from ambassador.models import Post

blog = Blueprint('blog', __name__)

@blog.route('/blog')
def Blog():
    posts = Post.query.all()  # Get all posts
    return render_template('blog.html', posts=posts)