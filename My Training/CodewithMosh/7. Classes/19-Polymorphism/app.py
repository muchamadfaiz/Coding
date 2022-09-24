# POLYMORPHISM
# refer to the ability of the function with the same name to carry different functionality altogether
# in this example our draw method taking many different forms
# 1. we could calling draw method on a text box
# 2. or we ca calling it on dropdownlist

from abc import ABC,abstractmethod


class UIControl(ABC):
    # with this decorator, This method has no implementation 
    # this class only define a contract or interface that all derivative should follow 
    @abstractmethod 
    def draw(self):
        pass


class TextBox(UIControl):
    # this class implement the draw method
    def draw (self):
        print("TextBox") # here is the implementation


class DropDownList(UIControl):
    # this class implement the draw method
    def draw (self):
        print("DropDownList") # here is the implementation


# def draw (control): # getting control object
#     control.draw()

def draw (controls):  # getting a list of control object
    for control in controls:
        control.draw()


ddl = DropDownList() # Creating object "ddl" 
# print(isinstance(ddl, UIControl))
# >> True -> coz ddl is an instance of "UIControl" class
# draw(ddl)

textbox = TextBox() 
# draw(textbox) # we pass a textbox function
draw([ddl,textbox])