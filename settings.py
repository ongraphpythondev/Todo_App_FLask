from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#Creating an instance of the flask app
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///vinay.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
