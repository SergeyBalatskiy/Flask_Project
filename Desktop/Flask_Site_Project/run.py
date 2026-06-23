from app.models import app, db

# Создание БД
with app.app_context():
    db.create_all()

# Запуск
if __name__ == "__main__":
    app.run(debug=True)


 
 