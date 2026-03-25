students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    ch = input("Choice: ")

    if ch == "1":
        name = input("Name: ")
        courses = input("Courses (comma): ").split(",")
        students[name] = courses

    elif ch == "2":
        for name in students:
            print(name, "->", students[name])

    elif ch == "3":
        break