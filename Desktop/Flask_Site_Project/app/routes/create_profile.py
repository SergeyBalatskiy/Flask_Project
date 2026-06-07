from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from app.models import Users, db, Questionnaire, app
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from app.forms import AddProfile
from werkzeug.utils import secure_filename
import os

create_pr = Blueprint("create_profile", __name__)

@create_pr.route("/create_profile", methods=["POST", "GET"])
@login_required
def create_profile():

    form = AddProfile()

    if form.validate_on_submit():
        files_filenames = []
        for file in form.photo_of_target_body.data:
            file_filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER_TARGET_BODY"]), file_filename)
            files_filenames.append(file_filename)
        # И ПОТОМ КОНЕЧНЫЙ СПИСОК МОЖНО БУДЕТ ДОБАВИТЬ В САМУ БД, А ПОТОМ УЖЕ ИЗ этого брать все названия фото и вставлять в анкету!

        create_quest = Questionnaire(
                id_of_user = current_user.id,
                age = form.age.data, 
                gender = form.gender.data, 
                height = form.height.data, 
                weight = form.weight.data, 
                target_weight = form.target_weight.data,
                target_of_training = form.target_of_training.data, 
                experience_of_training = form.experience_of_training.data,
                active_in_the_day = form.active_in_the_day.data,
                photo_of_target_body = form.photo_of_target_body.data,
                health_problems = form.health_problems.data,
                Report = form.Report.data
                )
        try:
            db.session.add(create_quest)
            db.session.commit()
            return redirect(url_for("profile.profile_of_user"))

        except Exception as e:

            print("Ошибка:", e)
            return "При обработке произошла ошибка. Возможно, вы некорректно ввели требуемые данные! Попробуйте повторить еще раз."

    
    return render_template("registration.html", form = form)
