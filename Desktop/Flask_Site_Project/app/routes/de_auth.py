from flask import Blueprint, redirect, url_for, flash
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)

de_auth = Blueprint("de_auth", __name__)

@de_auth.route("/logout_user")
@login_required
def deauth():
    logout_user()
    flash("Вы вышли из аккаунта", category="success")
    return redirect(url_for("authenitication.auth"))
