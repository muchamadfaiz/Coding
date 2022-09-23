#INHERITANCE
# in programming we have concept called DRY (Don't repeat yourself)
# there is 2 solutin 
# 1. Inheritance -> mechanism that allow us to define the common behaviour or common function 
#                 -> in one class and then inherit them in other classes
# 2. Composition

class Animal:
    def eat(self):
        print("eat")

# to simply inherit behaviour of other class we add parenthesis and input the name of the class
# in this example we input the class "animal" to class "mammal"
# Animal : Parent, Base
# Mammal : Child, Sub
class Mamal(Animal):  
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")


        