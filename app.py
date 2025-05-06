from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:12345@localhost/testalembic"

db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(100), nullable=False, unique=True)
  phone = db.Column(db.String(10), nullable=False, unique=True)

if __name__ == "__main__":
  app.run(debug=True)