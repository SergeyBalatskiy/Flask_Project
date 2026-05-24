from flask import Blueprint, render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash
from app.models import Users, db
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)

registration_bp = Blueprint("registration", __name__)


@registration_bp.route("/create_account", methods=["POST", "GET"])
def registration():

    if current_user.is_authenticated:

        return redirect(url_for("profile.profile_of_user"))

    if request.method == "POST":

        print(f"Все данные формы:{request.form}")

        name = request.form["name"]
        surname = request.form["surname"]
        password_hash = generate_password_hash(request.form["password"])
        mail = request.form["mail"]
        phone = request.form["phone"]

        new_user = Users(
            name=name,
            surname=surname,
            password_hash=password_hash,
            mail=mail,
            phone=phone,
        )

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("profile.profile_of_user"))

        except Exception as e:

            print("Ошибка:", e)
            return "При обработке произошла ошибка. Возможно, вы некорректно ввели требуемые данные! Попробуйте повторить еще раз."

    else:
        return render_template("registration.html")
