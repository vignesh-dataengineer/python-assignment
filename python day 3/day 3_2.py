
# Section 3: Nested Loop

# 16
for i in range(1, 5):
    print("*" * i)

# 17
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end="")
    print()

# 18
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i}x{j}={i*j}", end="  ")
    print()

# 19
for i in range(3):
    for m in ['A', 'B', 'C']:
        print(m, end=" ")
print()

# 20
for i in range(1, 10):
    print(i, end=" ")
print()