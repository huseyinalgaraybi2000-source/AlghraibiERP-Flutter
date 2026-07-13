from database import connect


def run():
    while True:
        print("\n===== Customers Module =====")
        print("1- Add Customer")
        print("2- View Customers")
        print("3- Edit Customer")
        print("4- Delete Customer")
        print("5- Back")

        choice = input("Choose: ")

        db = connect()
        cur = db.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS customers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                phone TEXT,
                address TEXT
            )
        """)

        if choice == "1":
            name = input("Customer Name: ")
            phone = input("Phone: ")
            address = input("Address: ")

            cur.execute(
                "INSERT INTO customers(name, phone, address) VALUES (?, ?, ?)",
                (name, phone, address)
            )

            db.commit()
            print("Customer Added Successfully")

        elif choice == "2":
            cur.execute("SELECT * FROM customers")
            rows = cur.fetchall()

            if rows:
                for row in rows:
                    print(
                        f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]} | Address: {row[3]}"
                    )
            else:
                print("No Customers Found")

        elif choice == "3":
            customer_id = input("Customer ID: ")
            name = input("New Name: ")
            phone = input("New Phone: ")
            address = input("New Address: ")

            cur.execute(
                "UPDATE customers SET name=?, phone=?, address=? WHERE id=?",
                (name, phone, address, customer_id)
            )

            db.commit()
            print("Customer Updated Successfully")

        elif choice == "4":
            customer_id = input("Customer ID: ")

            cur.execute(
                "DELETE FROM customers WHERE id=?",
                (customer_id,)
            )

            db.commit()
            print("Customer Deleted Successfully")

        elif choice == "5":
            db.close()
            break

        else:
            print("Wrong Choice")

        db.close()
