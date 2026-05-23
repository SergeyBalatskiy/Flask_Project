from flask import Blueprint, render_template, request, session, redirect, url_for
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)

de_auth = Blueprint("de_auth", __name__)


@de_auth.route("/de_auth")
@login_required
def deauth():
    logout_user()
    return redirect(url_for("authenitication.auth"))
