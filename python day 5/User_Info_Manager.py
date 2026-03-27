def create_user(name, age, role):
    return {
        "name": name.title(),
        "age": age,
        "role": role
    }

users = []

# Adding users
users.append(create_user("vicky", 22, "data engineer"))
users.append(create_user("saran", 25, "system engineer"))

print("All Users:")
for user in users:
    print(user)