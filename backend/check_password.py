import sqlite3

conn = sqlite3.connect("ai_teacher.db")
cursor = conn.cursor()

cursor.execute("SELECT email, password FROM students")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()