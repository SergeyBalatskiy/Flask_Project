import sqlite3

conn = sqlite3.connect("C:/Users/OS/Desktop/Flask_Site_Project/app/database/users.db")
cursor = conn.cursor()

# Показать все столбцы в таблице users
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()
#cursor.execute('DELETE FROM Users WHERE id = "1"')
for user in users:
  print(user)
conn.close()

