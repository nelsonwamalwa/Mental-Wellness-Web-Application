import sys
import os
from flask import Flask
from ambassador import db, bcrypt  # Import db, bcrypt, etc. from your Flask app module
from ambassador.models import User  # Import your User model

# Adjust the sys path as needed to locate your Flask application
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ambassador import create_app

def create_admin():
    app = create_app()  # Create the Flask app
    with app.app_context():  # Ensure you're within the application context
        hashed_password = bcrypt.generate_password_hash('Password').decode('utf-8')
        admin = User(username='Admin', email='admin@ambassadorswellnesscentre.com', password=hashed_password, is_admin=True)
        db.session.add(admin)
        db.session.commit()

# if __name__ == '__main__':
#     create_admin()
