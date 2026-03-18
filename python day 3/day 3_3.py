
# Section 4: String Basics

# 21
s = input("\nEnter string: ")
count = 0
for _ in s:
    count += 1
print("Length:", count)

# 22
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Vowels:", count)

# 23
count = 0
for ch in s:
    if ch.isalpha() and ch not in vowels:
        count += 1
print("Consonants:", count)

# 24
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed:", rev)

# 25
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")