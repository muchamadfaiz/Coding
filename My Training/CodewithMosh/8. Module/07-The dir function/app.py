# THE DIR FUNCTION 
# dir function "dir()" is used to debugging
from ecommerce.shopping import sales

# print(dir(sales))
print(sales.__name__) # print the name of the module
print(sales.__package__) # print the name of the package
print(sales.__file__) # print the address of the file (path)