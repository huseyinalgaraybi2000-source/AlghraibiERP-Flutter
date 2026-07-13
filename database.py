import sqlite3

DB = "erp.db"


def connect():
    return sqlite3.connect(DB)


def create_tables():
    conn = connect()
    cur = conn.cursor()

    # Employees
    cur.execute("""
    CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT
    )
    """)

    # Inventory
    cur.execute("""
    CREATE TABLE IF NOT EXISTS items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        quantity INTEGER,
        price REAL
    )
    """)

    # Sales
    cur.execute("""
    CREATE TABLE IF NOT EXISTS sales(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT,
        quantity INTEGER,
        price REAL
    )
    """)

    # Customers
    cur.execute("""
    CREATE TABLE IF NOT EXISTS customers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        address TEXT
    )
    """)

    # Suppliers
    cur.execute("""
    CREATE TABLE IF NOT EXISTS suppliers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        address TEXT
    )
    """)

    # Purchases
    cur.execute("""
    CREATE TABLE IF NOT EXISTS purchases(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        supplier TEXT,
        item TEXT,
        quantity INTEGER,
        price REAL
    )
    """)

    # Invoices
    cur.execute("""
    CREATE TABLE IF NOT EXISTS invoices(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        invoice_date TEXT,
        total REAL
    )
    """)

    # Invoice Items
    cur.execute("""
    CREATE TABLE IF NOT EXISTS invoice_items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        invoice_id INTEGER,
        item_id INTEGER,
        quantity INTEGER,
        price REAL
    )
    """)

    conn.commit()
    conn.close()


# ================= Employees =================

def add_employee(name, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO employees(name, phone) VALUES(?, ?)",
        (name, phone)
    )
    conn.commit()
    conn.close()


def get_employees():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    conn.close()
    return rows


def update_employee(emp_id, name, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "UPDATE employees SET name=?, phone=? WHERE id=?",
        (name, phone, emp_id)
    )
    conn.commit()
    conn.close()


def delete_employee(emp_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM employees WHERE id=?",
        (emp_id,)
    )
    conn.commit()
    conn.close()


# ================= Inventory =================

def add_item(name, quantity, price):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO items(name, quantity, price) VALUES(?, ?, ?)",
        (name, quantity, price)
    )
    conn.commit()
    conn.close()


def get_items():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM items")
    rows = cur.fetchall()
    conn.close()
    return rows


def update_item(item_id, name, quantity, price):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "UPDATE items SET name=?, quantity=?, price=? WHERE id=?",
        (name, quantity, price, item_id)
    )
    conn.commit()
    conn.close()


def delete_item(item_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM items WHERE id=?",
        (item_id,)
    )
    conn.commit()
    conn.close()


def update_item_quantity(name, qty):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT quantity FROM items WHERE name=?",
        (name,)
    )

    row = cur.fetchone()

    if row:
        new_qty = row[0] - qty
        if new_qty < 0:
            new_qty = 0

        cur.execute(
            "UPDATE items SET quantity=? WHERE name=?",
            (new_qty, name)
        )

    conn.commit()
    conn.close()


# ================= Sales =================

def add_sale(item, quantity, price):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO sales(item, quantity, price) VALUES(?, ?, ?)",
        (item, quantity, price)
    )

    conn.commit()
    conn.close()


def get_sales():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM sales")
    rows = cur.fetchall()
    conn.close()
    return rows


def update_sale(sale_id, item, quantity, price):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE sales SET item=?, quantity=?, price=? WHERE id=?",
        (item, quantity, price, sale_id)
    )

    conn.commit()
    conn.close()


def delete_sale(sale_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM sales WHERE id=?",
        (sale_id,)
    )

    conn.commit()
    conn.close()
