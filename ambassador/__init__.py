from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login.Login'
login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from ambassador.pages.home import home
    from ambassador.pages.about import about
    from ambassador.pages.account import account
    from ambassador.pages.admin_posts import admin
    from ambassador.pages.article import article
    from ambassador.pages.blog import blog
    from ambassador.pages.comment import comment
    from ambassador.pages.contact import contact
    from ambassador.pages.create_post import create_post
    from ambassador.pages.layout import layout
    from ambassador.pages.post import post  
    from ambassador.pages.register import register
    from ambassador.pages.services import services
    from ambassador.pages.login import login
    from ambassador.pages.logout import logout

    app.register_blueprint(home)
    app.register_blueprint(about)
    app.register_blueprint(account)
    app.register_blueprint(admin)
    app.register_blueprint(article)
    app.register_blueprint(blog)
    app.register_blueprint(comment)
    app.register_blueprint(contact)
    app.register_blueprint(create_post)
    app.register_blueprint(layout)
    app.register_blueprint(post)  
    app.register_blueprint(register)
    app.register_blueprint(services)
    app.register_blueprint(login)
    app.register_blueprint(logout)

    return app

app = create_app()
