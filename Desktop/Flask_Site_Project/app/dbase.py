import sqlite3

try:

    connection = sqlite3.connect(
        "C:/Users/OS/Desktop/Flask_Site_Project/app/database/users.db"
    )
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE Users SET avatar = 'default.png' WHERE avatar = 'user_1.jpg'"
    )

    connection.commit()

    print("Все ок!")

    connection.close()

except Exception as e:
    print(e)
