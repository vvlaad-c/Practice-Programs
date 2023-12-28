# Small program for practicing using classes in coding
# requirements --> make a small application in the python enviroment that can track 
# the amount of employees are leaving and coming to a business, using classes in python

# Roles --> Employee, Manager, CEO

# creating the parent class
class Employee:

    def __init__(self, name, age, company_name, role):
        self.name = name
        self.age = age
        self.company_name = company_name
        self.role = role
    
    def say_role(self):
        print(f"My name is {self.name}, I am an {self.role} and I work at {self.company_name}")
    
    def permissions(self):
        print(f"My role in the company {self.company_name} is employee")
        print("My permissions let me acces the staff room and the break room")
    
    def say_age(self):
        print(f"I am {self.age} years old")

# creating the other classes which will inherit from the parent class
class Manager(Employee):

    def __init__(self, name, age, company_name, role):
        super().__init__(name, age, company_name, role)
    
    def say_role(self):
        print(f"My name is {self.name}, I am a {self.role} and I work at {self.company_name}")
        
    def permissions(self):
        print(f"My role at {self.company_name} is {self.role}")
        print("My permissions let me acces the staff room, the break room and the manager's office")
    
    def say_age(self):
        return super().say_age()

class CEO(Employee):
    
    def __init__(self, name, age, company_name, role):
        super().__init__(name, age, company_name, role)
    
    def say_role(self):
        print(f"My name is {self.name}, I work at {self.company_name} and I am a {self.role}")

    def permissions(self):
        print(f"My role at {self.company_name} is {self.role}")
        print("My permissions let me acces the staff room, the break room, the manager's office and the CEO office")
    
    def say_age(self):
        return super().say_age()

e1 = Employee("Vlad", 23, "Apple", "Employee")
e2 = Manager("Sorin", 45, "Microsoft", "Manager")
e3 = CEO("Matei", 34, "Uber", "CEO")

# Testing the parent class, Employee
e1.say_role()
e1.permissions()
e1.say_age()

# Testing the other classes which inherit from the parent class
# Manager
e2.say_role()
e2.permissions()
e2.say_age()

# CEO
e3.say_role()
e3.permissions()
e3.say_age()