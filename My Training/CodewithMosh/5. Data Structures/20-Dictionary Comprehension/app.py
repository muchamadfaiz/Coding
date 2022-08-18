# Dictionary Comprehension
# values = []
# for x in range(5):
#     values.append(x * 2)
# print(values)

#cleaner code
# [expression(do what?) for item(loop variable) in items(iterable)]
values = [x * 2 for x in range(5)] # we get list
print(values)

values = {x * 2 for x in range(5)} # we get set
print(values)

# what is the difference between dictionary and sets
"""
{1, 2, 3, 5} --> sets
{1: "a", 2: "b", 3: "c", 4: "d"} --> dictionary, key:values
"""

# [expression(do what?) for item(loop variable) in items(iterable)]
values = {x: x * 2 for x in range(5)} # we get set
print(values)