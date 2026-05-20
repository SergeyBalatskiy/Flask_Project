# Тут для базы данных что то
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///C:/Users/OS/Desktop/Flask_Site_Project/app/database/users.db"
)
app.config["SECRET_KEY"] = "05a8fe372941bef498a572c53b6aa1df1c8d3e27"
db = SQLAlchemy(app)


@app.errorhandler(404)
def error_handler_http(error):
    print(error)
    return render_template("error_handler.html")


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    mail = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    type_of_user = db.Column(db.String(10), default = "user")
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):

        return "<Article %r>" % self.id

    class Questionnaire(db.Model):
        id_of_user = db.Column(db.Integer, primary_key=True)
        age = db.Column(db.Integer, nullable=False)
        gender = db.Column(db.String(50), nullable=False)
        height = db.Column(db.Float, nullable=False)
        weight = db.Column(db.Float, nullable=False)
        targer_weight = db.Column(db.Float, nullable=False)
        target_of_training = db.Column(db.String(750), nullable=False)
        experience_of_training = db.Column(db.Integer, nullable=False)
        photo_of_target_body = db.Column(db.BLOB, nullable=False)
        health_problems = db.Column(db.String(1000), nullable=False)
        Report = db.Column(db.String(100), nullable=False)
        user_date = db.Column(db.DateTime, default=datetime.utcnow)

        def __repr__(self):

            return "<Article %r>" % self.id
