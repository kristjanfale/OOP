# __init__ is one of the Special Methods

# The goal of __repr__ is to be unambiguous (nedvoumno). It's good for developers, for debugging

# The goal of __str__ is to be readable. It's good for non-developers, it looks more friendly

class Employee:

    raise_amount = 1.04   # This is a class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)   # If we want to access class variable, we need to access it
                                                       # through the class itself or through instance of a class

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee("Kristjan", "Fale", 50000)   # This is an instance of the class Employee
emp_2 = Employee("Test", "User", 60000)   # This is an instance of the class Employee

print(emp_1)
# print(repr(emp_1))  = print(emp_1.__repr__())
# print(str(emp_1))  = print(emp_1.__str__())

print(emp_1 + emp_2)  # If we didn't have __add__ this would give a error:
                      # TypeError: unsupported operand type(s) for +: 'Employee' and 'Employee'

print(len(emp_1))
