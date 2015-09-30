from flask import Flask

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

auth = Flask(__name__)
auth.config.from_pyfile('config.py')
db = SQLAlchemy(auth)

from auth import views, models
