from database import connect


def inventory_report():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM items")
    rows = cursor.fetchall()

    print("\n===== Inventory Report =====")
    if rows:
        for row in rows:
            print(row)
    else:
        print("No inventory data found.")

    conn.close()


def sales_report():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sales")
    rows = cursor.fetchall()

    print("\n===== Sales Report =====")
    if rows:
        for row in rows:
            print(row)
    else:
        print("No sales data found.")

    conn.close()


def employees_report():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    print("\n===== Employees Report =====")
    if rows:
        for row in rows:
            print(row)
    else:
        print("No employees data found.")

    conn.close()


def invoices_report():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT invoices.id,
               customers.name,
               invoices.invoice_date,
               invoices.total
        FROM invoices
        JOIN customers
        ON invoices.customer_id = customers.id
    """)

    rows = cursor.fetchall()

    print("\n===== Invoices Report =====")

    if rows:
        for row in rows:
            print(
                f"Invoice:{row[0]} | Customer:{row[1]} | Date:{row[2]} | Total:{row[3]}"
            )
    else:
        print("No invoices data found.")

    conn.close()


def run():
    while True:
        print("\n===== Reports Module =====")
        print("1- Inventory Report")
        print("2- Sales Report")
        print("3- Employees Report")
        print("4- Invoices Report")
        print("5- Back")

        choice = input("Choose: ")

        if choice == "1":
            inventory_report()

        elif choice == "2":
            sales_report()

        elif choice == "3":
            employees_report()

        elif choice == "4":
            invoices_report()

        elif choice == "5":
            break

        else:
            print("Wrong Choice")
