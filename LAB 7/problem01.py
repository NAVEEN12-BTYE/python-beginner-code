# PPMS - Product Price Management System (Beginner Code)

products = {
    "Apple": 50,
    "Banana": 20,
    "Orange": 30,
    "Mango": 60,
    "Grapes": 40
}

def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    products[name] = price
    print("Product added.")

def update_price():
    name = input("Enter product name to update: ")
    if name in products:
        price = float(input("Enter new price: "))
        products[name] = price
        print("Price updated.")
    else:
        print("Product not found.")

def delete_product():
    name = input("Enter product name to delete: ")
    if name in products:
        del products[name]
        print("Product deleted.")
    else:
        print("Product not found.")

def total_price():
    total = 0
    for p in products.values():
        total = total + p
    print("Total price =", total)

def discount():
    per = float(input("Enter discount %: "))
    for key in products:
        products[key] = products[key] - (products[key] * per / 100)
    print("Discount applied.")

def show_products():
    print("Products:")
    for key, value in products.items():
        print(key, ":", value)


# Simple Menu
while True:
    print("\n1.Add  2.Update  3.Delete  4.Total  5.Discount  6.Show  7.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        add_product()
    elif ch == 2:
        update_price()
    elif ch == 3:
        delete_product()
    elif ch == 4:
        total_price()
    elif ch == 5:
        discount()
    elif ch == 6:
        show_products()
    elif ch == 7:
        break
    else:
        print("Invalid choice")
