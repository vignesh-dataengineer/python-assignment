employees = []

while True:
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        role = input("Enter role: ")
        salary = input("Enter salary: ")

        emp = {
            "name": name,
            "age": age,
            "role": role,
            "salary": salary
        }

        employees.append(emp)
        print("Employee added!")

    elif choice == "2":
        if len(employees) == 0:
            print("No employees found")
        else:
            for emp in employees:
                print(emp)

    elif choice == "3":
        name = input("Enter name to update: ")
        found = False

        for emp in employees:
            if emp["name"] == name:
                emp["role"] = input("New role: ")
                emp["salary"] = input("New salary: ")
                print("Updated!")
                found = True

        if not found:
            print("Employee not found")

    elif choice == "4":
        name = input("Enter name to delete: ")
        found = False

        for emp in employees:
            if emp["name"] == name:
                employees.remove(emp)
                print("Deleted!")
                found = True
                break

        if not found:
            print("Employee not found")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")