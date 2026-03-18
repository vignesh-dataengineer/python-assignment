# ---------------- TASK 35 ----------------
# Job eligibility program

age_task35_input = int(input("Enter age for task 35: "))
height_task35_input = int(input("Enter height for task 35 (cm): "))
weight_task35_input = int(input("Enter weight for task 35 (kg): "))

if age_task35_input >= 18:
    if height_task35_input >= 160:
        if weight_task35_input >= 60:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")


# ---------------- TASK 36 ----------------
# College admission program

marks_task36_input = int(input("Enter marks for task 36: "))
age_task36_input = int(input("Enter age for task 36: "))

if marks_task36_input >= 60:
    if age_task36_input >= 17:
        print("Admission Granted")
    else:
        print("Admission Rejected")
else:
    print("Admission Rejected")


# ---------------- TASK 37 ----------------
# Sports selection program

age_task37_input = int(input("Enter age for task 37: "))
height_task37_input = int(input("Enter height for task 37 (cm): "))
weight_task37_input = int(input("Enter weight for task 37 (kg): "))

if age_task37_input >= 16:
    if height_task37_input >= 150:
        if weight_task37_input >= 50:
            print("Selected for Sports")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")