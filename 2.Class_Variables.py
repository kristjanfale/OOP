class Employee:

    num_of_emp = 0
    raise_amount = 1.04   # This is a class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"

        Employee.num_of_emp += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)    # If we want to access class variable we need to access it
                                                        # through the class itself or through instance of a class
        # self.pay = int(self.pay * Employee.raise_amount)

print(Employee.num_of_emp)   # = 0

emp_1 = Employee("Kristjan", "Fale", 50000)   # This is an instance of the class Employee
emp_2 = Employee("Test", "User", 60000)   # This is an instance of the class Employee


print(Employee.num_of_emp)   # = 2


emp_1.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
