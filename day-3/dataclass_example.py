from dataclasses import dataclass


@dataclass
class Person:
    """
    A simple data class to represent a person's information.
    
    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        gender (str): The gender of the person.
    """
    name: str
    age: int
    gender: str


# Creating an instance of the Person class
person = Person(name="Alice", age=25, gender="Female")

# Accessing fields of the person instance
print("Name:", person.name)
print("Age:", person.age)
print("Gender:", person.gender)

# String representation (automatically generated)
print("Person object:", person)
