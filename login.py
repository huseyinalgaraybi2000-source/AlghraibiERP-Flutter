import sqlite3

conn = sqlite3.connect("erp.db")
cursor = conn.cursor()

username = input("Username: ")
password = input("Password: ")

cursor.execute(
"SELECT * FROM users WHERE username=? AND password=?",
(username, password)
)

user = cursor.fetchone()

conn.close()

if user:
    print("Login Successful")
else:
    print("Wrong Username or Password")
