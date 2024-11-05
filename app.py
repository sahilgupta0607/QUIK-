from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.debug = True 

class Users(db.Model):
    userID = db.Column(db.Integer, primary_key = True)
    password = db.Column(db.String(50))
    role = db.Column(db.String(50))


if __name__ == '__main__': 
    app.run()


