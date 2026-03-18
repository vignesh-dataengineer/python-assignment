# Section 7: List Operations

lst = [100, 200, 300]

# 36
lst.append(400)
lst.append(500)
lst.append(600)
print("\nAfter append:", lst)

# 37
lst.insert(1, 150)
print("After insert:", lst)

# 38
lst.remove(200)
print("After remove:", lst)

# 39 (reverse without reverse())
rev = []
for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])
print("Reversed:", rev)

# 40 (sort without sort())
lst2 = [5, 2, 8, 1]
for i in range(len(lst2)):
    for j in range(i+1, len(lst2)):
        if lst2[i] > lst2[j]:
            lst2[i], lst2[j] = lst2[j], lst2[i]
print("Sorted:", lst2)