# Tuples
# tuple is read only list, we cant modify that list (add, remove, etc)

point = 1, 2
print(type(point))

point = 1,
print(type(point))

point = 1
print(type(point))

point = ()
print(type(point))

point = (1, 2) + (3, 4)
print(point)

point = (1, 2) * 3
print(point)

point = tuple([1, 2])
print(point)

point = tuple("Hello World")
print(point)

point = (1, 2, 3)
print(point[0:2])

x, y, z = point
if 10 in point:
    print("exist")

# point[0] = 10 --> error tuples object does not support item assignment
# to prevent accidental error in modifying some sequence
