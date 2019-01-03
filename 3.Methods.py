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
        self.pay = int(self.pay * self.raise_amount)   # If we want to access class variable we need to access it
                                                       # through the class itself or through instance of a class
        # self.pay = int(self.pay * Employee.raise_amount)


    @classmethod   # This is altering the functionality of our method. So now we receive the class(cls) as a first argument instead of the instance(self)
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_strings(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)   # This creates and returns a new employee


    @staticmethod   # This methods don't take a class or instance as a first argument
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:   # If it is Sunday or Saturday
            return False
        return True


emp_1 = Employee("Kristjan", "Fale", 50000)   # This is an instance of the class Employee
emp_2 = Employee("Test", "User", 60000)   # This is an instance of the class Employee

# STATICMETHODS
import datetime
my_date = datetime.date(2018, 12, 23)

print(Employee.is_workday(my_date))

# CLASSMETHODS
emp_str_1 = "John-Doe-80000"
emp_str_2 = "Bob-Elvis-40000"
emp_str_3 = "Emily-Doe-70000"

new_emp_1 = Employee.from_strings(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)