from database import connect


def run():
    while True:
        print("\n===== Invoices Module =====")
        print("1- Create Invoice")
        print("2- View Invoices")
        print("3- Delete Invoice")
        print("4- Back")

        choice = input("Choose: ")

        db = connect()
        cur = db.cursor()

        if choice == "1":
            customer_id = input("Customer ID: ")

            cur.execute(
                "SELECT id, name FROM customers WHERE id=?",
                (customer_id,)
            )

            customer = cur.fetchone()

            if customer is None:
                print("Customer not found.")
                db.close()
                continue

            cur.execute(
                "INSERT INTO invoices(customer_id, invoice_date, total) VALUES(?, date('now'), ?)",
                (customer_id, 0)
            )

            invoice_id = cur.lastrowid
            total = 0

            while True:
                print("\nAvailable Items:")

                cur.execute(
                    "SELECT id, name, quantity, price FROM items"
                )

                items = cur.fetchall()

                for item in items:
                    print(
                        f"{item[0]} - {item[1]} | Qty:{item[2]} | Price:{item[3]}"
                    )

                item_id = input("\nItem ID (0 = Finish): ")

                if item_id == "0":
                    break

                qty = int(input("Quantity: "))

                cur.execute(
                    "SELECT quantity, price FROM items WHERE id=?",
                    (item_id,)
                )

                row = cur.fetchone()

                if row is None:
                    print("Item not found.")
                    continue

                stock = row[0]
                price = row[1]

                if qty > stock:
                    print("Not enough stock.")
                    continue

                total += qty * price

                cur.execute(
                    "INSERT INTO invoice_items(invoice_id, item_id, quantity, price) VALUES(?,?,?,?)",
                    (invoice_id, item_id, qty, price)
                )

                cur.execute(
                    "UPDATE items SET quantity = quantity - ? WHERE id=?",
                    (qty, item_id)
                )

            cur.execute(
                "UPDATE invoices SET total=? WHERE id=?",
                (total, invoice_id)
            )

            db.commit()

            print("Invoice Saved Successfully")
            print(f"Total: {total}")

        elif choice == "2":
            cur.execute("""
                SELECT invoices.id,
                       customers.name,
                       invoices.invoice_date,
                       invoices.total
                FROM invoices
                JOIN customers
                ON invoices.customer_id = customers.id
            """)

            rows = cur.fetchall()

            if rows:
                for row in rows:
                    print(
                        f"Invoice:{row[0]} | Customer:{row[1]} | Date:{row[2]} | Total:{row[3]}"
                    )
            else:
                print("No Invoices Found")

        elif choice == "3":
            invoice_id = input("Invoice ID: ")

            cur.execute(
                "DELETE FROM invoice_items WHERE invoice_id=?",
                (invoice_id,)
            )

            cur.execute(
                "DELETE FROM invoices WHERE id=?",
                (invoice_id,)
            )

            db.commit()

            print("Invoice Deleted Successfully")

        elif choice == "4":
            db.close()
            break

        else:
            print("Wrong Choice")

        db.close()
