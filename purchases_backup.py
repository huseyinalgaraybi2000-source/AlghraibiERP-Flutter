from database import connect


def run():
    while True:
        print("\n===== Purchases Module =====")
        print("1- Add Purchase")
        print("2- View Purchases")
        print("3- Delete Purchase")
        print("4- Back")

        choice = input("Choose: ")

        db = connect()
        cur = db.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS purchases(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                supplier TEXT,
                item TEXT,
                quantity INTEGER,
                price REAL
            )
        """)

        if choice == "1":
            supplier = input("Supplier Name: ")
            item = input("Item Name: ")
            qty = int(input("Quantity: "))
            price = float(input("Purchase Price: "))

            # التأكد من وجود المنتج
            cur.execute(
                "SELECT id FROM items WHERE name=?",
                (item,)
            )

            row = cur.fetchone()

            if row:
                cur.execute(
                    "UPDATE items SET quantity = quantity + ? WHERE name=?",
                    (qty, item)
                )
            else:
                cur.execute(
                    "INSERT INTO items(name, quantity, price) VALUES(?,?,?)",
                    (item, qty, price)
                )

            cur.execute(
                "INSERT INTO purchases(supplier, item, quantity, price) VALUES(?,?,?,?)",
                (supplier, item, qty, price)
            )

            db.commit()
            print("Purchase Added Successfully")

        elif choice == "2":
            cur.execute("SELECT * FROM purchases")
            rows = cur.fetchall()

            if rows:
                for row in rows:
                    print(
                        f"ID:{row[0]} | Supplier:{row[1]} | Item:{row[2]} | Qty:{row[3]} | Price:{row[4]}"
                    )
            else:
                print("No Purchases Found")

        elif choice == "3":
            purchase_id = input("Purchase ID: ")

            cur.execute(
                "DELETE FROM purchases WHERE id=?",
                (purchase_id,)
            )

            db.commit()
            print("Purchase Deleted Successfully")

        elif choice == "4":
            db.close()
            break

        else:
            print("Wrong Choice")

        db.close()
