users = {"admin": "1234", "user": "pass"}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login Successful")
else:
    print("Invalid Login")