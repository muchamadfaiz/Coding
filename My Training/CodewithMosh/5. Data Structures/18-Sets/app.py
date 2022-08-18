# sets
# Remove duplicate, 
numbers = [1, 1, 2, 3, 4]
# uniques = set(numbers)
# second = {1, 4}
# second.app(5)
# second.remove(5)
# len(second)
# print(uniques)

first = set(numbers)
second = {1, 5}

print(first | second) # "|" union the data
print(first & second) # "&" intersecting the data
print(first - second) # "-" the difference about datas
print(first ^ second) # "^" will return the data neither in the first or second set

# set doesnt support indexing
# set is an unordered collection of unique items not in sequence, so we cant acces them using an index, 
# we cant have a duplicate