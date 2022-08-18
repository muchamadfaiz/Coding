# Generator Expression
# values = [x * 2 for x in range(10)]
# for x in values:
#     print(x)



# value is no longer a list, it's generator object
# generator object more efficient in handling big data
# values = (x * 2 for x in range(10)) 
# print(values)
# for x in values:
#     print(x)

# Call function to know the size of data
from sys import getsizeof
values = (x * 2 for x in range(10000000)) # the size of data --> 104 bytes
print("gen", getsizeof(values), "bytes")
values = [x * 2 for x in range(10000000)] # the size of data --> 89095160 bytes
print("list", getsizeof(values), "bytes")
