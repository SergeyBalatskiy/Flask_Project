from flask import Blueprint, session, redirect, url_for, render_template, flash, request, make_response
from app.models import ALLOWED_EXTENSIONS, app
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from werkzeug.utils import secure_filename
import os

profile = Blueprint("profile", __name__)


def allowed_file(filename):
    """Функция проверки расширения файла"""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@profile.route("/profile")
@login_required
def profile_of_user():

    return render_template("profile.html")

@profile.route("/upload_avatar")
@login_required
def upload_avatar():
    
    ...

@profile.route("/show_avatar")
@login_required
def show_avatar():
    ...