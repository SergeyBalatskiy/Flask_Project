from flask import (
    Blueprint,
    redirect,
    url_for,
    render_template,
    flash
)
from app.models import app, Users, db, Questionnaire
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)
import os
import shutil


delete_user = Blueprint("delete_user", __name__)

@delete_user.route("/delete")
@login_required
def delete():
    
    #Удаляется анкета с фото тела
    quest_to_delete = Questionnaire.query.filter_by(id_of_user=current_user.id).first()
    if quest_to_delete:
        try:
            upload_path = os.path.join(app.config["UPLOAD_FOLDER_TARGET_BODY"], str(current_user.id))
            try:
                shutil.rmtree(upload_path)
            except Exception as e:
                print(e)
                flash("Возникла непредвиденная ошибка при удалении ваших фото", category="error")
                return redirect(url_for("profile.profile_of_user"))

            db.session.delete(quest_to_delete)
            db.session.commit()

        except Exception as e:
            print(f"Произошла ошибка {e}")
            flash(f"Ошиба типа:{e}", category="error")
            return redirect(url_for("profile.profile_of_user"))

    # Удаляется фото аватар (если оно у него есть)    
    if current_user.avatar != "default.png":
        os.remove(os.path.join(app.config["UPLOAD_FOLDER"], current_user.avatar))

    # И удаляется сам аккаунт
    user_to_remove = Users.query.get(current_user.id)

    try:
        db.session.delete(user_to_remove)
        db.session.commit()
        logout_user()
        flash("Вы успешно удалили свой аккаунт!", category="success")
        return redirect(url_for("main_page.main"))
    except Exception as e:
        print(e)
        flash("Возникла непредвиденная ошибка при удалении ваших фото", category="error")
        return redirect(url_for("profile.profile_of_user"))


@delete_user.route("/confirm_to_delete_user")
@login_required
def confirm_to_delete():

    return render_template("confirm_to_delete_user.html")
