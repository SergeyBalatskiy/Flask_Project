from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from app.models import Users, db
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from app.forms import RegisterForm

registration_bp = Blueprint("registration", __name__)

@registration_bp.route("/create_account", methods=["POST", "GET"])
def registration():

    if current_user.is_authenticated:

        return redirect(url_for("profile.profile_of_user"))

    # Берется форма на базе класса и применяется для регистрации 
    form = RegisterForm()

    # Если кнопка нажата:
    if form.validate_on_submit():

        password_hash_regist = generate_password_hash(form.password_hash.data)
        new_user = Users(
            name=form.name.data,
            surname=form.surname.data,
            password_hash=password_hash_regist,
            mail=form.mail.data,
            phone=form.phone.data,
            avatar = "default.png"
        )

        # Проверка на существование уже такой почты
        q = db.session.query(Users).filter(Users.mail == form.mail.data)

        if db.session.query(q.exists()).scalar():
            flash("Пользователь с такой почтой уже зарегистрирован!", category="error")
            return render_template("registration.html", form = form)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("profile.profile_of_user"))
        
        except Exception as e:
            print("Ошибка:", e)
            return "При обработке произошла ошибка. Возможно, вы некорректно ввели требуемые данные! Попробуйте повторить еще раз."

    # Передача шаблона формы для рендера
    return render_template("registration.html", form = form)


