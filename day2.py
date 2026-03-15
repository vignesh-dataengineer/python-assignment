# Task 1

# AND
a = 10
b = 6
print("AND:", a & b)

#Task 2
# OR
x = 12
y = 5
print("OR:", x | y)

#Task 3
# NOT
num = 8
print("NOT:", ~num)

#Task 4
# XOR
a1 = 15
b1 = 9
print("XOR:", a1 ^ b1)

#Task 5
# Left shift
num1 = 7
print("Left Shift:", num1 << 2)

#Task 6
# Right shift
num2 = 20
print("Right Shift:", num2 >> 1)

#Task 7 & *
# User input
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print("AND result:", n1 & n2)
print("XOR result:", n1 ^ n2)


# Task 9
# Replication
s = "hi"
result1 = s * 4
print(result1)

# Task 10
s1 = "python"
result2 = s1 * 3
print(result2)

# Task 11
# Concatenation using +
a = "super"
b = "man"
result3 = a + b
print(result3)

# Task 12
a1 = "hello"
b1 = " "
c1 = "world"
result4 = a1 + b1 + c1
print(result4)

# Task 13
name = input("Enter your name: ")
result5 = name * 5
print(result5)

# Task 14
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
result6 = str1 + str2
print(result6)


# Task 15
# Take a name and print its data type
name_input = input("Enter your name: ")
print("Data type of name:", type(name_input))

# Task 16
# Take age and convert to integer
age_input = input("Enter your age: ")
age_integer = int(age_input)
print("Age after type casting:", age_integer)
print("Data type:", type(age_integer))

# Task 17
# Take two numbers and print their sum
num1_sum = int(input("Enter first number: "))
num2_sum = int(input("Enter second number: "))
sum_result = num1_sum + num2_sum
print("Sum:", sum_result)

# Task 18
# Take two marks and print average
mark1_avg = float(input("Enter first mark: "))
mark2_avg = float(input("Enter second mark: "))
average_result = (mark1_avg + mark2_avg) / 2
print("Average:", average_result)

# Task 19
# Calculate 3*a*2 + b - 2
a_expr = int(input("Enter value of a: "))
b_expr = int(input("Enter value of b: "))
expression_result = 3 * a_expr * 2 + b_expr - 2
print("Result:", expression_result)

# Task 20
# Print data type before and after type casting
num_input = input("Enter a number: ")
print("Before type casting:", type(num_input))

num_casted = int(num_input)
print("After type casting:", type(num_casted))


# Task 21
num_string_21 = input("Enter a number (string): ")
print("Last digit:", num_string_21[-1])

# Task 22
number_22 = int(input("Enter a number: "))
print("Unit digit:", number_22 % 10)

# Task 23
number_23 = int(input("Enter a number: "))
print("Number after removing last digit:", number_23 // 10)

# Task 24
number_24 = int(input("Enter a number: "))
print("Second last digit:", (number_24 // 10) % 10)

# Task 25
number_25 = int(input("Enter a 5 digit number: "))
print("Last digit of 5 digit number:", number_25 % 10)


# ---------------- TASK 26 ----------------
# Check if 10 ≥ 5

if 10 >= 5:
    print("10 is greater than or equal to 5")


# ---------------- TASK 27 ----------------
# Check if number is greater than 50

number_task_27_input = int(input("Enter a number for task 27: "))

if number_task_27_input > 50:
    print("Number is greater than 50")


# ---------------- TASK 28 ----------------
# Check if age ≥ 18

age_task_28_input = int(input("Enter your age for task 28: "))

if age_task_28_input >= 18:
    print("Age is 18 or above")


# ---------------- TASK 29 ----------------
# Check if number is greater than 100

number_task_29_input = int(input("Enter a number for task 29: "))

if number_task_29_input > 100:
    print("Number is greater than 100")


# ---------------- TASK 30 ----------------
# Check if number ≥ 0

number_task_30_input = int(input("Enter a number for task 30: "))

if number_task_30_input >= 0:
    print("Number is greater than or equal to 0")