import sqlite3

print("Alghraibi ERP Started")

conn = sqlite3.connect("erp.db")
print("Database Connected")
conn.close()

from screens.menu import main

if __name__ == "__main__":
    main()
