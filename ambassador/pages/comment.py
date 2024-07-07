from flask_login import current_user, login_required
from flask import url_for, flash, redirect, abort
from ambassador.models import User, Post, Comment, Like
from ambassador import db
from flask import Blueprint

comment = Blueprint('comment', __name__)


@comment.route("/comment/<int:comment_id>/delete", methods=['POST'])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if comment.author != current_user:
        abort(403)
    db.session.delete(comment)
    db.session.commit()
    flash('Your comment has been deleted!', 'success')
    return redirect(url_for('post', post_id=comment.post.id))

@comment.route("/like/<int:post_id>", methods=['POST'])
@login_required
def like_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author == current_user:
        abort(403)
    like = Like.query.filter_by(user_id=current_user.id, post_id=post.id).first()
    if like:
        db.session.delete(like)
        db.session.commit()
    else:
        like = Like(user_id=current_user.id, post_id=post.id)
        db.session.add(like)
        db.session.commit()
    return redirect(url_for('home'))