from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from app.models import Users, db, Questionnaire
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)

create_pr = Blueprint("create_profile", __name__)


@create_pr.route("/create_profile", methods=["POST", "GET"])
@login_required
def create_profile():

    if request.method == "POST":

        print(f"Все данные формы:{request.form}")

        age = request.form["age"]
        gender = request.form["gender"]
        height = request.form["height"]
        weight = request.form["weight"]
        targer_weight = request.form["targer_weight"]
        target_of_training = request.form["target_of_training"]
        experience_of_training = request.form["experience_of_training"]
        photo_of_target_body = request.form["photo_of_target_body"]
        health_problems = request.form["health_problems"]
        Report = request.form["report"]
        user_date = request.form["height"]

        new_profile = Questionnaire(
            id_of_user=current_user.id,
            age=age,
            gender=gender,
            height=height,
            weight=weight,
            targer_weight=targer_weight,
            target_of_training=target_of_training,
            experience_of_training=experience_of_training,
            photo_of_target_body=photo_of_target_body,
            health_problems=health_problems,
            Report=Report,
            user_date=user_date,
        )

        try:
            db.session.add(new_profile)
            db.session.commit()
            return redirect(url_for("profile.profile_of_user"))

        except Exception as e:

            print("Ошибка:", e)
            return "При обработке произошла ошибка. Возможно, вы некорректно ввели требуемые данные! Попробуйте повторить еще раз."

    else:
        return render_template("registration.html")
