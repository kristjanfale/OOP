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
        self.pay = int(self.pay * self.raise_amount)   # If we want to access class variable we need to access it
                                                       # through the class itself, or through instance of a class
        # self.pay = int(self.pay * Employee.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)   # Let the Employee class's init method handle the first, last and pay
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):   # employees=None - It is not good to pass in lists or
                                                            # dictionaries, so do it thi way
        super().__init__(first, last, pay)   # Let the Employee class's init method handle the first, last and pay
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("-->", emp.fullname())


dev_1 = Developer("Kristjan", "Fale", 50000, "Python")   # This is an instance of the class Employee
dev_2 = Developer("Test", "User", 60000, "Java")   # This is an instance of the class Employee

mgr_1 = Manager("Sue", "Miller", 90000, [dev_1])


# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emp()

print(isinstance(mgr_1, Manager))   # Is mgr_1 an instance of Manager --> True
print(issubclass(Developer, Manager))   # Is Developer a subclass of Manager --> False