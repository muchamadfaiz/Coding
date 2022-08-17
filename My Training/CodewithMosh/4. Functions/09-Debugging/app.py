"""
Debugging
F5 = Run Python Debug Console
F9 = insert Break Point
F11 = shifting into another function
F10 = go to next function
"""




def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("Start")
print(multiply(1,2,3))