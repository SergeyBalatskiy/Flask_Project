from flask import Blueprint, render_template

authenitication = Blueprint("authenitication", __name__)


@authenitication.route("/auth")
def auth():
    return render_template("auth.html")
