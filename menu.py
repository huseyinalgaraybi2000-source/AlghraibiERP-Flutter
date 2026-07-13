import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import create_tables

create_tables()

from screens import employees
from screens import inventory
from screens import sales
from screens import customers
from screens import suppliers
from screens import purchases
from screens import invoices
from screens import reports


def main():
    while True:
        print("\n==== Alghraibi ERP Menu ====")
        print("1- Employees")
        print("2- Inventory")
        print("3- Sales")
        print("4- Customers")
        print("5- Suppliers")
        print("6- Purchases")
        print("7- Invoices")
        print("8- Reports")
        print("9- Exit")

        choice = input("Choose: ")

        if choice == "1":
            employees.run()

        elif choice == "2":
            inventory.run()

        elif choice == "3":
            sales.run()

        elif choice == "4":
            customers.run()

        elif choice == "5":
            suppliers.run()

        elif choice == "6":
            purchases.run()

        elif choice == "7":
            invoices.run()

        elif choice == "8":
            reports.run()

        elif choice == "9":
            print("Exit ERP")
            break

        else:
            print("Wrong Choice")


if __name__ == "__main__":
    main()
