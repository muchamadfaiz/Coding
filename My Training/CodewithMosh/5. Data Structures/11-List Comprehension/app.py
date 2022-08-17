#  List Comprehension
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

#list comprehension vs map
prices = list(map(lambda item :item[1], items))
print(prices)

# prices = [expression for item in items]
prices = [item[1] for item in items]
print(prices)

#list comprehension vs filter
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
# prices = [expression for item in items]
prices = [item for item in items if item[1] >= 10]
print(prices)