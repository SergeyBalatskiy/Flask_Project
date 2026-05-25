import sqlite3

conn = sqlite3.connect("C:/Users/OS/Desktop/Flask_Site_Project/app/database/users.db")
cursor = conn.cursor()

# Показать все столбцы в таблице users
cursor.execute("PRAGMA table_info(users)")
columns = cursor.fetchall()

print("Столбцы в таблице users:")
for col in columns:
    print(f"  - {col[1]} ({col[2]})")

conn.close()