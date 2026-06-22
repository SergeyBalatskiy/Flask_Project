from app.models import app, db

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)


# Сделать визуализацию "нет анкеты?", поля для спрашивания о удалении, а также удаление всего аккаунта, а также админ роль((