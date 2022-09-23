# MULTI LEVEL INHERITANCE
# we know that inheritance is a good thing its prevent the duplicate of code
# but too much inheritance is a bad practice and increase complexity
# limit the level of inheritance to 1 - 2
# the methods you add in your classes are there to solve a business problem
# that is the focus of the software/program that you build
# its not because an animal can eat in a real world so you make class animal with method eat too
# just focus the method that solve ur problem
class Animal:
    def eat (self):
        print("eat")


class Bird (Animal):
    def fly (self):
        print("fly")

class Chicken(Bird):
    pass