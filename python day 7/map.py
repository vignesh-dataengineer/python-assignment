class Student:
    def __init__(self, name):
        self.name = name


students = [Student("Vicky"), Student("Deva")]

names = list(map(lambda s: s.name, students))

print(names)