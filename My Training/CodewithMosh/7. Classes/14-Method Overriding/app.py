# Method Overriding
# it is replacing/extending a method defined in the base class
# in this example we are extending the init method on Animal class

# basically method of subclass will replace/override the parent/super/base class if we dont use built in function super()

class Animals:
    def __init__ (self):
        print("Animal Constructor")
        self.age = 1
    
    def eat(self):
        print("eat")

class Mammals(Animals):
    def __init__ (self):
        super().__init__() #caling the init method on the parent class -> "Animals"
                           # if we dont write this line the constructor of Mammals will replace
                           # the constructor(init method) in its super class
        print("Mammals Constructor")
        self.weight = 2

    def walk (self):
        print("walk")

m = Mammals()
print(m.age)
print(m.weight)

# the constructor on the Mammals class will replace or override the constructor on the 
# Animal class, so when we wann call age atribute it raise an error cause no attribute age on instance "m"
# we can fix this with builtin function called super()