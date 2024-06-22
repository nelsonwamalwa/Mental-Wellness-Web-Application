# Mental Wellness Web Application

## Overview

This is a Flask-based web application designed to promote mental wellness. The application allows users to register, log in, view a blog, and access various services related to mental health. The backend is powered by SQLAlchemy with SQLite for development and PostgreSQL for production. The application also incorporates secure user authentication using Flask-Login and encrypted password storage.

## Features

- User registration and login with secure password hashing
- Blog section to post and view articles
- About, contact, and services pages
- Session management with Flask-Login
- Responsive design with Bootstrap (or another frontend framework)
- Dockerized for easy deployment

## Technologies Used

- **Flask**: Web framework
- **SQLAlchemy**: ORM for database interactions
- **SQLite/PostgreSQL**: Database (SQLite for development, PostgreSQL for production)
- **Flask-WTF**: Form handling and validation
- **Flask-Login**: User session management
- **Werkzeug**: Password hashing
- **Docker**: Containerization
- **Gunicorn**: WSGI HTTP server for deployment
- **Nginx**: Reverse proxy server

## Installation

### Prerequisites

- Python 3.8+
- Docker and Docker Compose (for containerized deployment)
- Node.js and npm (if using a frontend framework like Bootstrap)

### Clone the Repository

```bash
git clone https://github.com/yourusername/mental-wellness-app.git
cd mental-wellness-app
```

### Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up the Database

```bash
flask shell
>>> from ambassador.models import init_db
>>> init_db()
```

### Run the Application

```bash
flask run
```

### Running with Docker

Ensure Docker and Docker Compose are installed on your system.

```bash
docker-compose up --build
```

The application will be accessible at `http://localhost:8000`.

## Project Structure

```
Mental-Wellness-Web-Application/
│
├── ambassador/
│   ├── __init__.py
│   ├── models.py
│   ├── forms.py
│   └── routes.py
│
├── templates/
│   ├── layout.html
│   ├── about.html
│   ├── blog.html
│   ├── contact.html
│   ├── home.html
│   ├── login.html
│   └── register.html
│
├── static/
│   ├── css/
│   └── js/
│
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── nginx.conf
└── run.py
```

## Routes

- `/about`: About page
- `/blog`: Blog page to view posts
- `/contact`: Contact page
- `/home` or `/`: Home page
- `/services`: Services page
- `/register`: User registration
- `/login`: User login
- `/logout`: User logout

## Forms

### RegistrationForm

```python
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=10)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
```

### LoginForm

```python
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
```

## Security Considerations

- Passwords are hashed using `werkzeug.security.generate_password_hash`.
- User sessions are managed securely using Flask-Login.
- Ensure to set a strong secret key for Flask sessions.

## Deployment

### With Docker

1. Build and run the containers:

```bash
docker-compose up --build
```

2. The application will be accessible at `http://localhost`.

### Without Docker

1. Set up a WSGI server like Gunicorn:

```bash
gunicorn -b 0.0.0.0:8000 ambassador:app
```

2. Use a reverse proxy like Nginx to serve the application.

### Nginx Configuration

```nginx
server {
    listen 80;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## Contribution

Feel free to fork this repository and contribute by submitting a pull request. Please ensure your code adheres to the existing style and includes appropriate tests.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

For any questions or suggestions, please open an issue on GitHub or contact [wamalwanelson@gmail.com].