from abc import ABC, abstractmethod

class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


class Student(AbstractUser):
    def get_details(self):
        return "Student Details"