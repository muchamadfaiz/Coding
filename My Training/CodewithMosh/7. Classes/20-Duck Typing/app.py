# DUCK TYPING
# if it walks like a duck and quacks like a duck so it is a duck
# so to achieve polymorphic behaviour, we dont necessary need a base class like UI Control
# coz python supports duck typing

class TextBox:
    # this class implement the draw method
    def draw (self):
        print("TextBox") # here is the implementation


class DropDownList:
    # this class implement the draw method
    def draw (self):
        print("DropDownList") # here is the implementation


def draw (controls):  # getting a list of control object
    for control in controls:
        control.draw()


ddl = DropDownList() 
textbox = TextBox() 
draw([ddl,textbox])