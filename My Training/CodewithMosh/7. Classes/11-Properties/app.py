# # example 1
# class Product:
#     def __init__ (self, price):
#         # self.__price = price
#         self.set_price(price)

#     def get_price(self):
#         return self.__price

#     def set_price(self, value):
#         if value < 0:
#             raise ValueError("value cannot be negative")
#         self.__price = value
        
# mouse = Product(50)

# example 2 using property function
# property is an object that sits in front of attribute and allow us to get or set value

# class Product:
#     def __init__ (self, price):
#         # self.__price = price
#         self.set_price(price)

#     def get_price(self):
#         return self.__price

#     def set_price(self, value):
#         if value < 0:
#             raise ValueError("value cannot be negative")
#         self.__price = value
    
#     price = property(fget=get_price, fset=set_price)
        
# mouse = Product(50)
# mouse.price = 100
# print(mouse.price)

# example 3 using property
# with above code our problem is solved but we still can access that 2 methdo(get_price & set_price)
# this is polluting the interface of our object
# its like remote control having 5 button (so confusing)
# we want the remote control has a minimum button

class Product:
    def __init__ (self, price):
        # self.__price = price
        self.price = price

    @property
    def price(self): # this will make a property object called "price"
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("value cannot be negative")
        self.__price = value
    
        
mouse = Product(-50)
# mouse.__getattribute__
# mouse.price = 100
# print(mouse.price)