from User_Info_Manager import users

file = open("team_data.txt", "w")

for user in users:
    file.write(f"{user['name']} - {user['age']} - {user['role']}\n")

file.close()

# Reading file
file = open("team_data.txt", "r")
print("\nFile Content:")
print(file.read())

print("Is file closed?", file.closed)

file.close()