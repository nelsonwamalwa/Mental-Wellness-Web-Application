from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a12a39d53b5d254baf97a99d23026f7b'

from ambassador import routes
