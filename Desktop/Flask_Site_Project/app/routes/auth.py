from flask import Blueprint, render_template, request, session, redirect, url_for, flash
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
from app.forms import LoginForm

authenitication = Blueprint("authenitication", __name__)


@authenitication.route("/auth", methods=["POST", "GET"])
def auth():

    if current_user.is_authenticated:

        return redirect(url_for("profile.profile_of_user"))
    
    form = LoginForm()

    if form.validate_on_submit():
        mail_auth = form.email.data
        password_hash_auth = form.password.data
        rm = form.remember.data
        user = Users.query.filter_by(mail=mail_auth).first()

        if user and check_password_hash(user.password_hash, password_hash_auth):
            login_user(user, remember=rm)
 
            if not rm:
                session.permanent = False

            return redirect(
                request.args.get("next") or url_for("profile.profile_of_user")
            )
        else:
            flash("Введена неверная пара почта/пароль!", category="error")
            return redirect(url_for("authenitication.auth"))

    return render_template("auth.html", form = form)

