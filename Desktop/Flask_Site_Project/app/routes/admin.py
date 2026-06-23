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
from flask import send_file
from PIL import Image
from app.forms import AddProfile
from werkzeug.utils import secure_filename
import os

admin_security = Blueprint("admin", __name__)

# Перманентная проверка на доступ
@admin_security.before_request
def check_access():
    if current_user.type_of_user != "admin":

        return render_template("no_access.html")

@admin_security.route("/show_quest", methods = ["POST", "GET"])
@login_required
def show_questionaires():
    info = []

    if request.method == "POST":
        find_user = request.form["find_user"]

        print(find_user)

        try:
            query = db.session.query(Users)
            query = query.filter(Users.name.startswith(f'{find_user}'))
            info = query.all()
            print(info)
            return render_template("admin_quest.html", list = info)
        except Exception as e:
            flash(f"{e}", category="error")
            print(f"Произошла какая-то ошибка:{e}")
            return redirect(url_for("profile.show_profile_user"))

    try:
        info = Users.query.all()
    except Exception as e:
        print(f"Ошибка:{e}")
        flash(f"{e}", category="error")
        return redirect(url_for("profile.show_profile_user"))
    
    return render_template("admin_quest.html", list = info)

@admin_security.route("/user_detail/<int:u>")
@login_required
def show_quest(u):
    try:
        info = Users.query.get(u)
        info_quest = info.pr
        image_names = os.listdir(f"app/photo_of_target_body/{u}")
        print(f"{image_names}")

        return render_template("user_detail.html", info = info, info_quest = info_quest, image_names = image_names)   
    except Exception as e:
        return f"{e}"

@admin_security.route('/show_photo_body_admin/<int:user_id>/<filename>')
def show_photo_body(user_id, filename):
    base_path = app.config["UPLOAD_FOLDER_TARGET_BODY"]  

    full_path = os.path.join(base_path, str(user_id), filename)

    return send_file(full_path, mimetype='image/jpeg')



    



