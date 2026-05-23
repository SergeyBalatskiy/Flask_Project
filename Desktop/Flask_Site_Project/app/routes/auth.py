from flask import Blueprint, render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Users
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)

authenitication = Blueprint("authenitication", __name__)


@authenitication.route("/auth", methods=["POST", "GET"])
def auth():

    if current_user.is_authenticated:

        return redirect(url_for("profile.profile_of_user"))

    if request.method == "POST":

        mail_auth = request.form.get("mail")

        password_hash_auth = request.form.get("password")

        user = Users.query.filter_by(mail=mail_auth).first()

        if user and check_password_hash(user.password_hash, password_hash_auth):
            login_user(user)
            return redirect(url_for("profile.profile_of_user"))

    else:
        return render_template("auth.html")
