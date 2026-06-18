from flask import (
    Blueprint,
    session,
    redirect,
    url_for,
    render_template,
    flash,
    request,
    make_response,
)
from app.models import ALLOWED_EXTENSIONS, app, Users, db, Questionnaire
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from flask import send_file
from flask import send_from_directory
from werkzeug.utils import secure_filename
import os
from PIL import Image

profile = Blueprint("profile", __name__)


@profile.route("/")
@login_required
def profile_of_user():
    info = Users.query.get(current_user.id)
    info_quest = info.pr
    return render_template("profile.html", quest_list = info_quest)

@profile.route("/show_profile")
@login_required
def show_profile_user():

    info = []

    try:
        info = Users.query.get(current_user.id)
        info_quest = info.pr
        image_names = os.listdir(f"app/photo_of_target_body/{current_user.id}")
        return render_template("show_profile.html", info = info, info_quest = info_quest, image_names = image_names)   
    except Exception as e:
        return f"{e}"
     
def allowed_file(filename):
    """Функция проверки расширения файла"""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@profile.route('/show_photo_body/<filename>')
def show_photo_body(filename):

    base_path = app.config["UPLOAD_FOLDER_TARGET_BODY"]  
    full_path = os.path.join(base_path, str(current_user.id), filename)
    
    return send_file(full_path, mimetype='image/jpeg')

@profile.route("/show_avatar")
@login_required
def show_avatar():

    img = load_image()

    name_image = current_user.avatar

    indx = name_image.find(".")

    expansion = name_image[indx + 1 :]

    h = make_response(img)
    h.headers["Content-Type"] = f"image/{expansion}"

    return h


@profile.route("/upload_avatar", methods=["POST", "GET"])
@login_required
def upload_avatar():

    if request.method == "POST":

        if "file" not in request.files:

            flash("Ошибка загрузки файла", category="error")
            return redirect(url_for("profile.profile_of_user"))

        file = request.files["file"]

        if file.filename == "":

            flash("Ошибка загрузки файла", category="error")
            return redirect(url_for("profile.profile_of_user"))
        
        try:
            with Image.open(file) as img:
                img.verify()
            file.seek(0)
        except:
            check_name = secure_filename(file.filename)
            flash(f"Произошла ошибка при попытке проверить файл {check_name} на целостность/коректность!", category="error")
            return redirect(url_for("profile.profile_of_user"))
        
        if "file" and allowed_file(file.filename):

            file.seek(0)

            if current_user.avatar == "default.png":

                name_image = secure_filename(file.filename)

                indx = name_image.find(".")

                expansion = name_image[indx:].lower()

                obj_for_update = Users.query.get(current_user.id)

                filename_id = f"user_{current_user.id}{expansion}"

                obj_for_update.avatar = filename_id

                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename_id))

                try:
                    db.session.commit()
                    flash("Ваше новое фото успешно загружено!", category="success")
                    return redirect(url_for("profile.profile_of_user"))

                except Exception as e:
                    flash(f"При обработке произошла ошибка:{e}", category="error")
                    return redirect(url_for("profile.profile_of_user"))

            try:
                os.remove(
                    os.path.join(app.config["UPLOAD_FOLDER"], current_user.avatar)
                )

            except Exception as e:
                print(e)

            name_image = secure_filename(file.filename)

            indx = name_image.find(".")

            expansion = name_image[indx:].lower()

            filename_id = f"user_{current_user.id}{expansion}"


            if (expansion in current_user.avatar):
                print(expansion in current_user.avatar)

                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename_id))

            else:

                obj_for_update = Users.query.get(current_user.id)

                obj_for_update.avatar = filename_id

                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename_id))

                try:
                    db.session.commit()
                    flash("Ваше новое фото успешно загружено!", category="success")
                    return redirect(url_for("profile.profile_of_user"))

                except Exception as e:
                    flash(f"При обработке произошла ошибка:{e}", category="error")
                    return redirect(url_for("profile.profile_of_user"))
        else:
            flash(
                f"Некорректный файл! Пожалуйста, убедитесь что вы загружаете аватар с типом расширения '.jpg', '.jpeg' или '.png'.", category="error"
            )
            return redirect(url_for("profile.profile_of_user"))
    else:
        return redirect(url_for("profile.profile_of_user"))


def load_image():

    if current_user.avatar == "default.png":
        try:
            with app.open_resource(r"avatars_of_users/default.png", "rb") as f:
                img = f.read()
        except Exception as e:
            print("Возника ошибка:", e)

    else:
        name = current_user.avatar
        try:
            with app.open_resource(f"avatars_of_users/{name}", "rb") as f:
                img = f.read()
        except Exception as e:
            print("Возника ошибка:", e)

    return img
