class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees


students = [
    Student("Vicky", 60000),
    Student("Deva", 45000),
    Student("Sanju", 70000)
]

students.sort(key=lambda x: x.fees)

for s in students:
    print(s.name, s.fees)