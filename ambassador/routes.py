from flask import render_template, url_for, flash, redirect, request, session
from ambassador import app
from ambassador.models import db_session, User, Post
from ambassador.forms import RegistrationForm, LoginForm

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/blog')
def blog():
    posts = Post.query.all()
    logged_in_user = session.get('user')
    return render_template('blog.html', posts=posts, title='Blog', user=logged_in_user)

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/home')
@app.route('/')
def home():
    logged_in_user = session.get('user')
    return render_template('home.html', user=logged_in_user)

@app.route('/services')
def services():
    logged_in_user = session.get('user')
    return render_template('services.html', title='Services', user=logged_in_user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db_session.add(user)
        db_session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:  # Simplified password check
            session['user'] = user.username
            flash(f'You have been logged in successfully, {user.username}!', 'success')
            return redirect(url_for('blog'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

def create_db():
    """
    Creates the database tables.
    """
    init_db()
