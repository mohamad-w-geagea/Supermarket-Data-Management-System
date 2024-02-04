from Employees import *
from products_Inventory import *

def show_menu():
    print("###############################")
    print("Menu:")
    print("1. Employees")
    print("2. Product Inventory")
    print("0. Exit")
    print("###############################")

def show_employee_menu():
    print("###############################")
    print("Employee Menu:")
    print("1. Add Employee")
    print("2. Search for an Employee")
    print("3. Remove an Employee")
    print("4. Edit Employee Data")
    print("5. Print all Employees")
    print("0. Go back")
    print("###############################")

def show_product_menu():
    print("###############################")
    print("Product Inventory Menu:")
    print("1. Insert Product")
    print("2. Search for a Product")
    print("3. Sell Product")
    print("4. Show Sales Log")
    print("5. Print all Categories")
    print("6. Print all Brands for a category")
    print("0. Go back")
    print("###############################")

def add_employee(employee_tree):
    data = {}
    print("###############################")
    data["name"] = input("Enter employee name: ")
    data["age"] = int(input("Enter employee age: "))
    data["position"] = input("Enter employee position: ")
    data["salary"] = float(input("Enter employee salary: "))
    employee_tree.add_employee(data)
    print("Employee added successfully.")
    print("###############################")

def search_employee(employee_tree):
    print("###############################")
    employee_name = input("Enter employee name to search: ")
    employee_tree.search_employee(employee_name)
    print("###############################")
def remove_employee(employee_tree):
    print("###############################")
    employee_name = input("Enter employee name to remove: ")
    employee_tree.remove_employee(employee_name)
    print("###############################")

def edit_employee(employee_tree):
    print("###############################")
    employee_name = input("Enter employee name to edit: ")
    property_key = input("Enter property key to edit: ")
    new_value = input("Enter new value: ")
    employee_tree.edit_employee(employee_name, property_key, new_value)
    print("###############################")

def print_all_employees(employee_tree):
    print("###############################")
    print("All Employees:")
    employee_tree.print_all_employees()
    print("###############################")

def insert_product(product_inventory):
    print("###############################")
    name = input("Enter product name: ")
    category = input("Enter product category: ")
    brand = input("Enter product brand: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))

    product_inventory.insert_product(name, category, brand, price, quantity)
    print("Product inserted successfully.")
    print("###############################")
def search_product(product_inventory):
    print("###############################")
    category = input("Enter product category: ")
    brand = input("Enter product brand: ")
    name = input("Enter product name: ")

    product_inventory.search_product(category, brand, name)
    print("###############################")

def sell_product(product_inventory, sales_log):
    print("###############################")
    category = input("Enter product category: ")
    brand = input("Enter product brand: ")
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity to sell: "))

    product_inventory.sell_product(category, brand, name, quantity)
    sales_log.enqueue_sale(name, category, brand, product_inventory.get_product_price(category, brand, name))
    print("Product sold successfully.")
    print("###############################")

def show_sales_log(sales_log):
    print("###############################")
    print("Sales Log:")
    sales_log.print_sales_log()
    print("###############################")

def print_all_categories(product_inventory):
    print("###############################")
    print("All Categories:")
    product_inventory.categories.print_all_categories()
    print("###############################")
def print_all_brands(product_inventory):
    print("###############################")
    category = input("Enter category name: ")
    print("All Brands for Category:", category)
    product_inventory.print_all_brands(category)
    print("###############################")



inventory = ProductInventory()
products = open("products.txt","r")
product_list = products.readlines()
for product in product_list:
    args = product.split(", ")
    inventory.insert_product(args[0],args[1],args[2],args[3],args[4])
products.close()
sales_log = SalesLogQueue()
Supermarket_Employees_Tree = EmployeeBST()
emps = open("employees.txt","r")
empsl = emps.readlines()
Supermarket_Employees_List = []
for emp in empsl:
    args = emp.split(",")    
    Supermarket_Employees_List.append({"name": args[0], "position": args[1], "age": args[2], "salary": args[3]})
Supermarket_Employees_Tree.build_employee_tree(Supermarket_Employees_List)
emps.close()

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            show_employee_menu()
            employee_choice = input("Enter your choice: ")

            if employee_choice == "1":
                add_employee(Supermarket_Employees_Tree)
            elif employee_choice == "2":
                search_employee(Supermarket_Employees_Tree)
            elif employee_choice == "3":
                remove_employee(Supermarket_Employees_Tree)
            elif employee_choice == "4":
                edit_employee(Supermarket_Employees_Tree)
            elif employee_choice == "5":
                print_all_employees(Supermarket_Employees_Tree)
            elif employee_choice == "0":
                break
            else:
                print("###############################")
                print("Invalid choice. Please try again.")
                print("###############################")

    elif choice == "2":
        while True:
            show_product_menu()
            print("###############################")
            product_choice = input("Enter your choice: ")
            print("###############################")

            if product_choice == "1":
                insert_product(inventory)
            elif product_choice == "2":
                search_product(inventory)
            elif product_choice == "3":
                sell_product(inventory, sales_log)
            elif product_choice == "4":
                show_sales_log(sales_log)
            elif product_choice == "5":
                print_all_categories(inventory)
            elif product_choice == "6":
                print_all_brands(inventory)
            elif product_choice == "0":
                break
            else:
                print("###############################")
                print("Invalid choice. Please try again.")
                print("###############################")

    elif choice == "0":
        break
    else:
        print("###############################")
        print("Invalid choice. Please try again.")
        print("###############################")