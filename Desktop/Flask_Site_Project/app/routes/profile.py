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
from app.models import ALLOWED_EXTENSIONS, app
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


@profile.route("/profile")
@login_required
def profile_of_user():

    return render_template("profile.html")


@profile.route("/upload_avatar")
@login_required
def upload_avatar(): ...


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
