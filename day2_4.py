# ---------------- TASK 38 ----------------
# Print day name using match

day_number_task38 = int(input("Enter a number (1-7) for task 38: "))

match day_number_task38:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number")


# ---------------- TASK 39 ----------------
# Print color using match

color_number_task39 = int(input("Enter a number (1-3) for task 39: "))

match color_number_task39:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")
    case _:
        print("Invalid choice")


# ---------------- TASK 40 ----------------
# Print fruit using match

fruit_number_task40 = int(input("Enter a number (1-4) for task 40: "))

match fruit_number_task40:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")
    case _:
        print("Invalid choice")