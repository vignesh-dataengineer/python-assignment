accounts = {}

while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    ch = input("Choice: ")

    if ch == "1":
        name = input("Name: ")
        balance = float(input("Balance: "))
        accounts[name] = balance

    elif ch == "2":
        name = input("Name: ")
        amount = float(input("Deposit: "))
        if name in accounts:
            accounts[name] += amount

    elif ch == "3":
        name = input("Name: ")
        amount = float(input("Withdraw: "))
        if name in accounts and accounts[name] >= amount:
            accounts[name] -= amount

    elif ch == "4":
        name = input("Name: ")
        print("Balance:", accounts.get(name, 0))

    elif ch == "5":
        break