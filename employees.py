from database import connect

def run():
    while True:
        print("\n===== Employees Module =====")
        print("1- Add Employee")
        print("2- View Employees")
        print("3- Edit Employee")
        print("4- Delete Employee")
        print("5- Back")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Employee Name: ")
            job = input("Job: ")

            db = connect()
            cur = db.cursor()

            cur.execute("""
                CREATE TABLE IF NOT EXISTS employees(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    job TEXT
                )
            """)

            cur.execute(
                "INSERT INTO employees(name, job) VALUES(?, ?)",
                (name, job)
            )

            db.commit()
            db.close()

            print("Employee Added Successfully")

        elif choice == "2":
            db = connect()
            cur = db.cursor()

            cur.execute("""
                CREATE TABLE IF NOT EXISTS employees(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    job TEXT
                )
            """)

            cur.execute("SELECT id, name, job FROM employees")
            rows = cur.fetchall()

            if rows:
                for row in rows:
                    print(f"ID: {row[0]} | Name: {row[1]} | Job: {row[2]}")
            else:
                print("No Employees Found")

            db.close()

        elif choice == "3":
            emp_id = input("Employee ID: ")
            new_name = input("New Name: ")
            new_job = input("New Job: ")

            db = connect()
            cur = db.cursor()

            cur.execute(
                "UPDATE employees SET name=?, job=? WHERE id=?",
                (new_name, new_job, emp_id)
            )

            db.commit()
            db.close()

            print("Employee Updated Successfully")

        elif choice == "4":
            emp_id = input("Employee ID: ")

            db = connect()
            cur = db.cursor()

            cur.execute(
                "DELETE FROM employees WHERE id=?",
                (emp_id,)
            )

            db.commit()
            db.close()

            print("Employee Deleted Successfully")

        elif choice == "5":
            break

        else:
            print("Wrong Choice")
