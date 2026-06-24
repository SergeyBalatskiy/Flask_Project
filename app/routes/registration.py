from flask import Blueprint, render_template

registration_bp = Blueprint("registration", __name__)


@registration_bp.route("/create_account")
def registration():
    return render_template("registration.html")
