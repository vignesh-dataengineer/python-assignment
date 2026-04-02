class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees


students = [
    Student("Vicky", 60000),
    Student("Deva", 40000)
]

high_fee = list(filter(lambda s: s.fees > 50000, students))

for s in high_fee:
    print(s.name)