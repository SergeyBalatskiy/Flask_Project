from flask import Blueprint, render_template, request, session, redirect, url_for, flash

from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)

about_site_info = Blueprint("about_site", __name__)

@about_site_info.route("/about_site")
def about_site():
    return render_template("about_site.html")