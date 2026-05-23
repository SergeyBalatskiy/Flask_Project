from flask import Blueprint, session, redirect, url_for, render_template
from app.models import Users
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)

profile = Blueprint("profile", __name__)


@profile.route("/profile")
@login_required
def profile_of_user():

    user_object = current_user

    return render_template("profile.html", user_object=user_object)
