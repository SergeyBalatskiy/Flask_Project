from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, FileField, MultipleFileField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_wtf.file import FileAllowed

class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[Email("Некорректный email")])
    password = PasswordField("Пароль: ", validators=[DataRequired(), Length(min=5, max = 100,  message = "Пароль должен быть от 5 символов!")])
    remember = BooleanField("Запомнить", default=False)
    submit = SubmitField("Войти") 

class RegisterForm(FlaskForm):
    name = StringField("Имя: ", validators=[Length(min=2, max=50, message="Имя должно быть от 2 до 50 символов!")])
    surname = StringField("Фамилия: ", validators=[Length(min=4, max=80, message="Фамилия должна быть от 4 до 80 символов!")])
    password_hash = PasswordField("Пароль: ", validators=[DataRequired(message="Это поле должно быть заполнено обязательно!"), Length(min=5, max=100, message = "Длинна пароля должна быть от 5 символов!")])
    password_hash_2 = PasswordField("Повтор пароля: ", validators=[DataRequired(message="Это поле должно быть заполнено обязательно!"), EqualTo('password_hash', message = "Пароли не совпадают!" )])
    mail = StringField("Почта: ", validators=[DataRequired("Почта обязательна!"), Email(message = "Введен неверный формат почты. Пример: example@gmail.com"), Length(min=5, max=100, message="Почта должна быть длинной от 5 до 100 символов!")])
    phone = StringField("Телефон: ", validators=[Length(min=11, max=100, message="Номер телефона должен быть длинной от 11 до 100 символов!")])
    submit = SubmitField("Cоздать аккаунт") 

class AddProfile(FlaskForm):
    age = StringField("Возраст: ", validators = [DataRequired(message='Поле "Возраст" не должно быть пустым!')])
    gender = StringField("Пол: ", validators=[DataRequired(message='Поле "Пол" не должно быть пустым!')])
    height = StringField("Рост: ", validators = [DataRequired(message='Поле "Рост" не должно быть пустым!')])
    weight = StringField("Вес: ", validators=[DataRequired(message='Поле "Вес" не должно быть пустым!')])
    target_weight = StringField("Целевой вес: ", validators=[DataRequired(message='Поле "Целевой вес" не должно быть пустым!')])
    target_of_training = StringField("Цель тренировок: ", validators=[DataRequired(message='Поле "Цель тренировок" не должно быть пустым!')])
    experience_of_training = StringField("Стаж тренировок: ", validators = [DataRequired(message='Поле "Стаж тренировок" не должно быть пустым!')])
    active_in_the_day = StringField("Активность в течение дня: ", validators=[DataRequired(message='Поле "Активность в течение дня" не должно быть пустым!')])
    photo_of_target_body = MultipleFileField("Фото и уровень жира (текущая и желаемая форма)", validators=[DataRequired(message='Поле "Фото и уровень жира" не должно быть пустым!'), FileAllowed(["jpeg", "png", "jpg"], message = 'Необходимо загрузить фото в формате: "jpeg", "png", "jpg"')])
    health_problems = StringField("Проблемы со здоровьем: ", validators=[DataRequired(message='Поле "Проблемы со здоровьем" не должно быть пустым!')])
    Report = StringField("Комментарий: ")
    submit = SubmitField("Создать анкету") 