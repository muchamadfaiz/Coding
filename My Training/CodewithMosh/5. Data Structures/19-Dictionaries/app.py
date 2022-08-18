# Dictionary
# Phone Book
point = {"x":1, "y":2} # Key:Value
print(type(point))

point = dict(x=1, y=2) #keyword argument ex: x=1 (more clean than above)
print(point["x"]) # taking a value associated with a key using an index, index is the name of a key
                  # Dictionaries are collections of key value pairs, we cant acces them using a numerate index as we do with list
point["x"] = 10
point["z"] = 20

if "a" in point:
    print(point["a"])
else: 
    print("nothing")

print(point.get("a", 0))
del point["x"]
print(point)

for x in point:
    print(x)

for key in point:
    print(key, point[key])

for x in point.items(): # we get the touple
    print(x)

for key, value in point.items(): # we get the touple
    print(key,value)
