from functools import reduce

class Student:
    def __init__(self, fees):
        self.fees = fees


students = [Student(60000), Student(40000)]

total = reduce(lambda acc, s: acc + s.fees, students, 0)

print(total)