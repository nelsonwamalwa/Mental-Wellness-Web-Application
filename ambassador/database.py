from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def init_db(app):
    db.init_app(app)
    login_manager.init_app(app)

    # Configure your login manager settings (if needed)
    login_manager.login_view = 'login'
    login_manager.login_message_category = 'info'

    # Import models here to avoid circular imports
    from . import models
    
    return db

# Example of using this in your __init__.py or create_app() function:
# from database import init_db
# db = init_db(app)
