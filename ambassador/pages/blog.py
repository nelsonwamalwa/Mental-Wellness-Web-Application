from flask import render_template, Blueprint
from ambassador.models import Post

blog = Blueprint('blog', __name__)

@blog.route('/blog')
def Blog():
    posts = Post.query.order_by(Post.date_posted.desc()).all()  # Order posts by newest first
    return render_template('blog.html', posts=posts)
