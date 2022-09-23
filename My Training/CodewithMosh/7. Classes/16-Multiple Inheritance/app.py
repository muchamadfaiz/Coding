# Multiple Inheritance


class Employee:
    def greet(self):
        print("employee greet")


class Person:
    def greet(self):
        print("person greet")

    
class Manager(Employee, Person): # This is multiple inheritance
    pass

pawpaw = Manager()
pawpaw.greet()