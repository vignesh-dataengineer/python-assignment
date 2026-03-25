while True:
    name = input("Enter student name: ")
    m1 = int(input("Mark 1: "))
    m2 = int(input("Mark 2: "))
    m3 = int(input("Mark 3: "))

    total = m1 + m2 + m3
    avg = total / 3

    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print("\nReport Card")
    print("Name:", name)
    print("Total:", total)
    print("Average:", avg)
    print("Grade:", grade)

    ch = input("Continue? (y/n): ")
    if ch == "n":
        break