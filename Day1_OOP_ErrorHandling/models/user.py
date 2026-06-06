from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")