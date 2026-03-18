# Section 6: List Basics

# 31
lst = [1, 2, 3, 4, 5]
print("\nSum:", sum(lst))

# 32
print("Max:", max(lst))

# 33
print("Min:", min(lst))

# 34
count = 0
for _ in lst:
    count += 1
print("Count:", count)

# 35
x = int(input("Enter element to search: "))
if x in lst:
    print("Found")
else:
    print("Not Found")