from models.user import User
from exceptions.custom_exceptions import InvalidSalaryError

class Employee(User):

    def __init__(self, name, age, salary):

        super().__init__(name, age)

        if salary < 0:
            raise InvalidSalaryError(
                "Salary cannot be negative!"
            )

        self.__salary = salary

    def display(self):

        print("\nEmployee Details")
        print("----------------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.__salary}")