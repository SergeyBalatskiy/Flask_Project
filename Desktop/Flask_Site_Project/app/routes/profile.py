from flask import Blueprint, session, redirect, url_for, render_template
from app.models import Users

profile = Blueprint("profile", __name__)


@profile.route("/profile/<int:id>")
def profile_of_user(id):

    user_object = Users.query.get(id)

    print(type(session["authorised"]), type((user_object.id)))

    if user_object.id == session["authorised"]:

        return render_template("profile.html", user_object=user_object)

    else:
        return redirect(url_for("authenitication.auth"))
