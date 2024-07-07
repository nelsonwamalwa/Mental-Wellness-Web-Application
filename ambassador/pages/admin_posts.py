from flask_login import current_user,login_required
from flask import render_template, abort
from flask import Blueprint

admin = Blueprint('admin', __name__)


@admin.route("/admin/posts")
@login_required
def Admin_posts():
    # if not current_user.is_admin:
    #     current_app.logger.info(f"User {current_user.username} attempted to access admin page.")
    #     abort(403)  # Forbidden if not admin
    # posts = Post.query.filter_by(approved=False).all()
    # return render_template('admin_posts.html', posts=posts)
    return render_template('admin_posts.html')