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
from app.models import ALLOWED_EXTENSIONS, app, Users, db
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from werkzeug.utils import secure_filename
import os

profile = Blueprint("profile", __name__)


def allowed_file(filename):
    """Функция проверки расширения файла"""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


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

        file_data = file.read()

        if len(file_data) > 1024 * 1024:
            flash(
                "Разрешение файла слижком большое! Необходимо, чтобы размер файла был не больше 1 МБ!",
                category="error",
            )
            return redirect(url_for("profile.profile_of_user"))

        if "file" and allowed_file(file.filename):

            file.seek(0)

            if current_user.avatar == "default.png":

                name_image = secure_filename(file.filename)

                indx = name_image.find(".")

                expansion = name_image[indx:]

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

            # Посмотреть какой файл загружается????

            indx = name_image.find(".")

            expansion = name_image[indx:]

            filename_id = f"user_{current_user.id}{expansion}"

            print(f"💥{expansion}💥")

            print(f"✅{filename_id}✅")

            if (
                expansion in current_user.avatar
            ):  # Срабатывает именно это условие почему то!!!
                print(expansion in current_user.avatar)

                print(f"💥{expansion}💥")

                print(f"✅{current_user.avatar}✅")

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


@profile.route("/profile")
@login_required
def profile_of_user():

    print(current_user.avatar)

    return render_template("profile.html")


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
