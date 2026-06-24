from flask import (
    Blueprint,
    redirect,
    url_for,
    render_template,
    flash
)
from app.models import app, db, Questionnaire
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

delete_profile = Blueprint("delete_profile", __name__)

@delete_profile.route("/delete_profile")
@login_required
def delete_quest():

    # Получение обьекта на удаление
    quest_to_delete = Questionnaire.query.filter_by(id_of_user=current_user.id).first()

    print(quest_to_delete)

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
            flash("Ваша анкета успешно удалена!", category="success")
            return redirect(url_for("profile.profile_of_user"))

        except Exception as e:
            print(f"Произошла ошибка {e}")
            flash(f"Ошиба типа:{e}", category="error")
            return redirect(url_for("profile.profile_of_user"))
        
    else:
        flash("Ваша анкета еще не создана, чтобы удалить ее!", category="error")
        return redirect(url_for("profile.profile_of_user"))
    
@delete_profile.route("/confirm_to_delete")
@login_required
def confirm_to_delete():
    return render_template("confirm_to_delete.html")