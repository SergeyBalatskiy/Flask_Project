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
from PIL import Image
from app.forms import AddProfile
from werkzeug.utils import secure_filename
import os
from datetime import datetime

edit_pr = Blueprint("edit_pr", __name__)

@edit_pr.route("/edit_profile", methods=["POST", "GET"])
@login_required
def edit_profile():

    quest = Questionnaire.query.filter_by(id_of_user=current_user.id).first()
    
    if quest:
        form = AddProfile(obj = quest)
        form.submit.label.text = "Обновить анкету"
    else:
        return redirect(url_for('create_profile.create_profile'))

    if form.validate_on_submit():

        real_files = []

        for f in form.photo_of_target_body.data:
            if f and f.filename:
                real_files.append(f)

        for check_file in real_files:
            try:
                with Image.open(check_file) as img:
                    img.verify()
                check_file.seek(0)
            except:
                check_name = secure_filename(check_file.filename)
                flash(f"Произошла ошибка при попытке проверить файл {check_name} на целостность/коректность!", category="error")
                return render_template("profile_edit.html", form = form)

        upload_path = os.path.join(app.config["UPLOAD_FOLDER_TARGET_BODY"], str(current_user.id))

        files_filenames = []

        if real_files:

            image_names = os.listdir(f"app/photo_of_target_body/{current_user.id}")
            for i in image_names:
                os.remove(os.path.join(upload_path, i))

            try:
                os.makedirs(upload_path, exist_ok=True)
            except Exception as e:
                print(e)
                flash("Возникла непредвиденная ошибка при попытке сохранения фото.", category="error")
                return render_template("profile_edit.html", form=form)
            
            for file in real_files:
                file_filename = secure_filename(file.filename)
                file_path = os.path.join(upload_path, file_filename)
                try:
                    file.save(file_path)
                    files_filenames.append(file_filename)
                except:
                    flash("Обнаружен пустой файл", category="error")
                    return render_template("profile_edit.html", form = form)

            if not files_filenames:
                flash("Не удалось сохранить ни одно фото.", category="error")
                return render_template("profile.show_profile_user")
            else:
                photos_lst = ", ".join(files_filenames)
        
        else:
            photos_lst = quest.photo_of_target_body

        quest.age = form.age.data
        quest.gender = form.gender.data
        quest.height = form.height.data
        quest.weight = form.weight.data
        quest.target_weight = form.target_weight.data
        quest.target_of_training = form.target_of_training.data 
        quest.experience_of_training = form.experience_of_training.data
        quest.active_in_the_day = form.active_in_the_day.data
        quest.photo_of_target_body = photos_lst
        quest.health_problems = form.health_problems.data
        quest.Report = form.Report.data
        quest.user_date = datetime.now()

        print(datetime.utcnow())

        try:
            db.session.commit()
            flash("Ваша анкета успешно обновлена!", category="success")
            return redirect(url_for("profile.show_profile_user"))

        except Exception as e:
            print("Ошибка:", e)
            flash(f"Произошла ошибка:{e}")
            return redirect(url_for("profile.show_profile_user"))

    return render_template("profile_edit.html", form = form)