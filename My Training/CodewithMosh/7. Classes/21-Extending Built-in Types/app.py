# EXTENDING BUILT_IN TYPES

# we can inherit a class from a built in class like "str"
# so our class have all the function/method that the class "str" has
# this is called "EXTENDING BUILT-IN CLASS"
class Text(str):
    def duplicate(self): # "self" represent the current object, which is in this case an instance of a string class
        return self + self


# we can create a list method too
# class Trackable list is inherited from built-in "list" class
# so we extend the append method of the "list" class
class TrackableList(list):
    def append(self, object): # we override the append method
        print("Append called") # and impelement print, so when we call append there is a mesasage
        super().append(object) # and we call the "append" method of the base class


text = Text("Python")
print(text.lower()) # we can use lower method that "str" class has
# >> python
print(text.duplicate()) # and we can use duplicate method that we aleady create to extend "str" class
# >> PythonPython

lists = TrackableList() #create a list object using trackable list
lists.append("pawpaw") # so every time we use append method there will message "Append called"
# >> Append called 
print(lists)
 

paw = list()
paw.append("pawpaw")
print(paw)