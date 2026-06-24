from flask import Blueprint, render_template, redirect, url_for, flash
from app.models import db, Questionnaire, app
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from PIL import Image
from app.forms import AddProfile
from werkzeug.utils import secure_filename
import os

create_pr = Blueprint("create_profile", __name__)

# Создание анкеты
@create_pr.route("/create_profile", methods=["POST", "GET"])
@login_required
def create_profile():

    form = AddProfile()
    quest = Questionnaire.query.filter_by(id_of_user=current_user.id).first()

    if quest:
        print(quest)
        flash("У вас уже есть анкета!", category="success")
        return redirect(url_for("profile.show_profile_user"))
    
    if form.validate_on_submit():

        real_files = []

        for f in form.photo_of_target_body.data:
            if f and f.filename:
                real_files.append(f)

        if not real_files:
            flash("Загрузите хотя бы одно фото", category="error")
            return render_template("create_profile.html", form=form)

        for check_file in real_files:
            try:
                with Image.open(check_file) as img:
                    img.verify()
                check_file.seek(0)
            except:
                check_name = secure_filename(check_file.filename)
                flash(f"Произошла ошибка при попытке проверить файл {check_name} на целостность/коректность!", category="error")
                return render_template("create_profile.html", form = form)

        upload_path = os.path.join(app.config["UPLOAD_FOLDER_TARGET_BODY"], str(current_user.id))

        try:
            os.makedirs(upload_path, exist_ok=True)
        except Exception as e:
            print(e)
            flash("Возникла непредвиденная ошибка при попытке сохранения фото.", category="error")
            return render_template("create_profile.html", form=form)

        files_filenames = []

        for file in real_files:
            file_filename = secure_filename(file.filename)
            file_path = os.path.join(upload_path, file_filename)
            try:
                file.save(file_path)
            except:
                flash("Обнаружен пустой файл", category="error")
                return render_template("create_profile.html", form = form)
            
            files_filenames.append(file_filename)

        if not files_filenames:
            flash("Не удалось сохранить ни одного фото", category="error")
            return render_template("create_profile.html", form = form)
        
        photos_lst = ", ".join(files_filenames)

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
                photo_of_target_body = photos_lst,
                health_problems = form.health_problems.data,
                Report = form.Report.data
                )
        try:
            db.session.add(create_quest)
            db.session.commit()
            return redirect(url_for("profile.show_profile_user"))

        except Exception as e:
            print("Ошибка:", e)
            return "При обработке произошла ошибка. Возможно, вы некорректно ввели требуемые данные! Попробуйте повторить еще раз."

    return render_template("create_profile.html", form = form)
