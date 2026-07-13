from database import connect


def run():
    while True:
        print("\n===== Sales Module =====")
        print("1- Add Sale")
        print("2- View Sales")
        print("3- Delete Sale")
        print("4- Back")

        choice = input("Choose: ")

        if choice == "1":
            item = input("Item Name: ")
            qty = int(input("Quantity: "))

            db = connect()
            cur = db.cursor()

            cur.execute(
                "SELECT quantity, price FROM items WHERE name=?",
                (item,)
            )

            row = cur.fetchone()

            if row is None:
                print("Item not found.")
                db.close()
                continue

            stock_qty = row[0]
            unit_price = row[1]

            if qty > stock_qty:
                print("Not enough quantity in stock.")
                db.close()
                continue

            total = qty * unit_price

            cur.execute("""
                CREATE TABLE IF NOT EXISTS sales(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    item TEXT,
                    quantity INTEGER,
                    price REAL
                )
            """)

            cur.execute(
                "INSERT INTO sales(item, quantity, price) VALUES (?, ?, ?)",
                (item, qty, total)
            )

            cur.execute(
                "UPDATE items SET quantity = quantity - ? WHERE name=?",
                (qty, item)
            )

            db.commit()
            db.close()

            print("Sale Added Successfully")
            print(f"Total: {total}")

        elif choice == "2":
            db = connect()
            cur = db.cursor()

            cur.execute(
                "SELECT id, item, quantity, price FROM sales"
            )

            rows = cur.fetchall()

            if rows:
                for row in rows:
                    print(
                        f"ID: {row[0]} | Item: {row[1]} | Qty: {row[2]} | Total: {row[3]}"
                    )
            else:
                print("No Sales Found")

            db.close()

        elif choice == "3":
            sale_id = input("Sale ID: ")

            db = connect()
            cur = db.cursor()

            cur.execute(
                "DELETE FROM sales WHERE id=?",
                (sale_id,)
            )

            db.commit()
            db.close()

            print("Sale Deleted Successfully")

        elif choice == "4":
            break

        else:
            print("Wrong Choice")
