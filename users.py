import sqlite3

conn = sqlite3.connect("erp.db")
cursor = conn.cursor()

username = input("Username: ")
password = input("Password: ")

cursor.execute(
"INSERT INTO users (username, password) VALUES (?, ?)",
(username, password)
)

conn.commit()
conn.close()

print("User Created")
