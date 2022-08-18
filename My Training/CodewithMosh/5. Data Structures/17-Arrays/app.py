#  Array
from array import array

numbers = array("i", [1, 2, 3])
numbers.append(5)
x = numbers.pop(2)
print(x)
print(numbers)
numbers[0] = 4
print(numbers)