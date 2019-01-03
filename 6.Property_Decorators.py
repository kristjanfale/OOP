
class Employee:


    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = (first + "." + last + "@gmail.com").lower()

    @property  # We are defining email like it is a method, but we are able to access it like an attribute (emp_1.email)
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"

    @property # We are defining email like a method, but we are able to access it like an attribute (emp_1.fullname)
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter   # Name of the Setter Decorator is on of the names of the property decorator
    def fullname(self, name):   # name - the value, that we are trying to set
        first, last = name.split(" ")   # Split the name on two parts
        self.first = first
        self.last = last

    @fullname.deleter  # This gets run, whenever we delete an attribute (del emp_1.fullname)
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None


emp_1 = Employee("John", "Smith")   # This is an instance of the class Employee

emp_1.fullname = "Kristjan Fale"

print(emp_1.email)
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
del emp_1.fullname
print(emp_1.fullname)