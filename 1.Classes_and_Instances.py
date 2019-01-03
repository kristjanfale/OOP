class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"

    def fullname(self):
        return f"{self.first} {self.last}"

emp_1 = Employee("Kristjan", "Fale", 50000)   # This is an instance of the class Employee
emp_2 = Employee("Test", "User", 60000)   # This is an instance of the class Employee

print(emp_1.fullname())   # This two prints are the same
print(Employee.fullname(emp_1))