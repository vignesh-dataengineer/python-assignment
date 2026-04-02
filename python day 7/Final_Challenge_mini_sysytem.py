from abc import ABC, abstractmethod
from functools import reduce

# ==============================
# ABSTRACT CLASS
# ==============================
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


# ==============================
# BASE CLASS
# ==============================
class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id


# ==============================
# CHILD CLASSES
# ==============================
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"{self.name} | ID:{self.id} | Dept:{self.dept} | Fees:{self.fees}"


class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"{self.name} | ID:{self.id} | Salary:{self.salary}"


# ==============================
# DATA
# ==============================
students = [
    Student("Vicky", 1, "CSE", 60000),
    Student("Deva", 2, "ECE", 45000),
    Student("Sanju", 3, "IT", 70000)
]

faculty = [
    Faculty("Kamal", 101, 40000),
    Faculty("Raj", 102, 25000)
]


# ==============================
# PRINT ALL DETAILS
# ==============================
print("\n--- ALL DETAILS ---")
for s in students:
    print(s.get_details())

for f in faculty:
    print(f.get_details())


# ==============================
# SORTING
# ==============================
students.sort(key=lambda x: x.fees)
faculty.sort(key=lambda x: x.salary)

print("\n--- SORTED STUDENTS ---")
for s in students:
    print(s.name, s.fees)

print("\n--- SORTED FACULTY ---")
for f in faculty:
    print(f.name, f.salary)


# ==============================
# FILTER
# ==============================
high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

print("\n--- HIGH FEE STUDENTS ---")
for s in high_fee_students:
    print(s.name)

print("\n--- HIGH SALARY FACULTY ---")
for f in high_salary_faculty:
    print(f.name)


# ==============================
# MAP
# ==============================
names = list(map(lambda s: s.name, students))
print("\n--- STUDENT NAMES ---")
print(names)


# ==============================
# REDUCE
# ==============================
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print("\n--- TOTAL FEES ---")
print(total_fees)

print("\n--- TOTAL SALARY ---")
print(total_salary)


# ==============================
# HIGHER ORDER FUNCTION
# ==============================
def process_users(users, func):
    return list(map(func, users))

result = process_users(students, lambda s: s.name.upper())

print("\n--- PROCESSED NAMES ---")
print(result)