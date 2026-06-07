from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from flask import Flask, render_template, url_for
from flask_login import LoginManager
from flask_login import UserMixin

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///C:/Users/OS/Desktop/Flask_Site_Project/app/database/users.db"
)
app.config["SECRET_KEY"] = "05a8fe372941bef498a572c53b6aa1df1c8d3e27"
app.config["SESSION_PERMANENT"] = False
app.config["REMEMBER_COOKIE_DURATION"] = timedelta(days=2)
app.config["UPLOAD_FOLDER"] = (
    r"C:\Users\OS\Desktop\Flask_Site_Project\app\avatars_of_users"
)
app.config["UPLOAD_FOLDER_TARGET_BODY"] = (
    r"C:\Users\OS\Desktop\Flask_Site_Project\app\photo_of_target_body"
)
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
)
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = "authenitication.auth"
login_manager.login_message = "Авторизируйтесь для доступа к закрытым страницам"
login_manager.login_message_category = "warning"


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.after_request
def add_header(response):
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response

@app.errorhandler(404)
def error_handler_http(error):
    print(error)
    return render_template("error_handler.html")


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    mail = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    type_of_user = db.Column(db.String(10), default="user")
    avatar = db.Column(db.String(50), default="default.png")
    date = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def is_active(self):
        # Example: Only active if the user has verified their email
        return self.mail

    def __repr__(self):

        return "<Article %r>" % self.id


class Questionnaire(db.Model):
    id_of_user = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    target_weight = db.Column(db.Float, nullable=False)
    target_of_training = db.Column(db.String(750), nullable=False)
    experience_of_training = db.Column(db.Integer, nullable=False)
    active_in_the_day = db.Column(db.Strig(40), nullable = False)
    photo_of_target_body = db.Column(db.BLOB, nullable=False)
    health_problems = db.Column(db.String(1000), nullable=False)
    Report = db.Column(db.String, nullable=False)
    user_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):

        return "<Article %r>" % self.id
