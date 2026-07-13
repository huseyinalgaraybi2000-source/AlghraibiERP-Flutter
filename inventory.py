from database import connect

def run():
    while True:
        print("\n===== Inventory Module =====")
        print("1- Add Item")
        print("2- View Items")
        print("3- Edit Item")
        print("4- Delete Item")
        print("5- Back")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Item Name: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))

            db = connect()
            cur = db.cursor()

            cur.execute("""
                CREATE TABLE IF NOT EXISTS items(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    quantity INTEGER,
                    price REAL
                )
            """)

            cur.execute(
                "INSERT INTO items(name, quantity, price) VALUES(?, ?, ?)",
                (name, quantity, price)
            )

            db.commit()
            db.close()

            print("Item Added Successfully")

        elif choice == "2":
            db = connect()
            cur = db.cursor()

            cur.execute("SELECT id, name, quantity, price FROM items")
            rows = cur.fetchall()

            if rows:
                for row in rows:
                    print(f"ID: {row[0]} | Name: {row[1]} | Qty: {row[2]} | Price: {row[3]}")
            else:
                print("No Items Found")

            db.close()

        elif choice == "3":
            item_id = input("Item ID: ")
            name = input("New Name: ")
            quantity = int(input("New Quantity: "))
            price = float(input("New Price: "))

            db = connect()
            cur = db.cursor()

            cur.execute(
                "UPDATE items SET name=?, quantity=?, price=? WHERE id=?",
                (name, quantity, price, item_id)
            )

            db.commit()
            db.close()

            print("Item Updated Successfully")

        elif choice == "4":
            item_id = input("Item ID: ")

            db = connect()
            cur = db.cursor()

            cur.execute(
                "DELETE FROM items WHERE id=?",
                (item_id,)
            )

            db.commit()
            db.close()

            print("Item Deleted Successfully")

        elif choice == "5":
            break

        else:
            print("Wrong Choice")
