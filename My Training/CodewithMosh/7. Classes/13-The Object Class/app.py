# THE OBJECT CLASS
# All the class in the Python is an inheritance from "object" class
# in other "object" class is base object of every class in python

class Animals(): # actually Animals class is inheritance of "object" class -> Animals(object)
    def eat(self):
        print("eat")

class Mammals(Animals):    
    def walk(self):
        print("walk")

class Fish(Animals):
    def swim(self):
        print("swim")

kucing = Mammals()

# isinstance(instance, class)
print(isinstance(kucing, Mammals))
# >> True --> because kucing is an instance of "Mammals" Class
print(isinstance(kucing, Animals))
# >> True --> because Mammals inherit from Animals, so an instance of "Mammal "class is also an instance of "Animal" class
print(isinstance(kucing, Fish))
# >> False --> coz kucing is not an inheritance of class "Fish"
print(isinstance(kucing, object))
# >> True --> coz kucing is for sure an inheritance of base class "object"

# issubclass(subclass, class)
print(issubclass(Mammals, Animals))
# >> True --> coz Mammals is a subclass from class "Animals"
print(issubclass(Mammals, object))
# >> True --> coz Mammals is directly for sure a subclass from base class "object"

o = object() 
# instance ("o") has all the magic method in every class of python
kucing = Mammals()
# instance ("kucing") has all the magic method too because its inherits from class Mammals and 
# class Mammal inherit from base "object" class
