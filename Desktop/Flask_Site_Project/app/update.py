import sqlite3

conn = sqlite3.connect("C:/Users/OS/Desktop/Flask_Site_Project/app/database/users.db")
cursor = conn.cursor()

# Показать все столбцы в таблице users
cursor.execute('SELECT * FROM Users')
user = cursor.fetchall()
for col in user:
    print(col)
conn.close()
