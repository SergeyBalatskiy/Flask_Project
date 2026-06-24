import sqlite3
from app.models import Users, db
from datetime import datetime
from werkzeug.security import generate_password_hash
from app.models import app
from app.routes.main import main_bp
from app.routes.registration import registration_bp
from app.routes.profile import profile
from app.routes.auth import authenitication
from app.routes.de_auth import de_auth
from app.routes.create_profile import create_pr
from app.routes.about_site import about_site_info
from app.routes.profile_edit import edit_pr
from app.routes.delete_profile import delete_profile
from app.routes.delete_user import delete_user
from app.routes.admin import admin_security

# Инициализация блюпринтов
app.register_blueprint(main_bp, url_prefix = "/")
app.register_blueprint(registration_bp, url_prefix = "/create_user")
app.register_blueprint(profile, url_prefix = "/profile")
app.register_blueprint(authenitication, url_prefix = "/authentication")
app.register_blueprint(de_auth, url_prefix = "/de_auth")
app.register_blueprint(create_pr, url_prefix = "/create")
app.register_blueprint(about_site_info, url_prefix = "/about")
app.register_blueprint(edit_pr, url_prefix = "/edit")
app.register_blueprint(delete_profile, url_for= "/delete")
app.register_blueprint(delete_user, url_prefix = "/delete_user")
app.register_blueprint(admin_security, url_prefix = "/admin")

# Создание в БД при инициализации Админа 
with app.app_context():

    # Запрос на существование админа
    q = db.session.query(Users).filter(Users.type_of_user == "admin")

    # Он есть?
    if db.session.query(q.exists()).scalar():
        print("Пользователь уже зарегистрирован!")

    else:

        try:
            conn = sqlite3.connect("C:/Users/OS/Desktop/Flask_Site_Project/app/database/users.db")
            cursor = conn.cursor()

            password = generate_password_hash("158765")
            now_date = datetime.now()

            cursor.execute('INSERT INTO Users (name, surname, password_hash, mail, phone, type_of_user, avatar, date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', ('Евгений', 'Астафьевич', f'{password}', 'admin@bk.ru', '+79996217315', 'admin', 'default.png', f'{now_date}'))
            
            conn.commit()
            conn.close()
            print('Администратор создан!')
        except Exception as e:
            print(f"Ошибка при создании админа:{e}")
