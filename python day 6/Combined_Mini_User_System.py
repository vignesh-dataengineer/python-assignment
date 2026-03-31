class User:
    users_count = 0   # class variable

    def __init__(self, username, pwd):
        self.__username = username
        self.__pwd = pwd
        User.users_count += 1

    def get_user(self):
        return self.__username

    def register(self):
        print(f"{self.__username} registered")
        return self

    def login(self):
        print(f"{self.__username} logined")
        return self

    def greet(self):
        print("Welcome User")
        return self


class Student(User):
    def greet(self):
        print("Welcome Student")
        return self


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")
        return self


# Usage
s1 = Student("vignesh", "7777")
f1 = Faculty("messi", "1010")

s1.login().greet().register()
f1.login().greet().register()

print("Total users:", User.users_count)