
# Section 2: While Loop

# 11
i = 1
while i <= 20:
    print(i)
    i += 1

# 12
num = int(input("Enter number: "))
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print("Factorial:", fact)

# 13
num = int(input("Enter number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("Reversed:", rev)

# 14
num = int(input("Enter number: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print("Digits:", count)

# 15
print("\n15. Type 'stop' to exit")
while True:
    val = input("Enter something: ")
    if val == "stop":
        break
