cart = []

while True:
    print("\n1. Add Item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        name = input("Product: ")
        price = float(input("Price: "))
        qty = int(input("Quantity: "))

        cart.append({"name": name, "price": price, "qty": qty})
        print("Added!")

    elif ch == "2":
        total = 0
        for item in cart:
            sub = item["price"] * item["qty"]
            total += sub
            print(item["name"], "-", sub)
        print("Total:", total)

    elif ch == "3":
        name = input("Enter item to remove: ")
        for item in cart:
            if item["name"] == name:
                cart.remove(item)
                print("Removed!")
                break

    elif ch == "4":
        break