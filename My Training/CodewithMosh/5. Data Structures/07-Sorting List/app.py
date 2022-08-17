# Sorting list
# numbers = [2, 9, 100, 201, 21, 67]
# numbers.sort()
# print(numbers)

# numbers.sort(reverse = True)
# print(numbers)

# sorted(numbers)
# print(numbers)

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

def sort_item(items):
    return items[1]

items.sort(key = sort_item, reverse=True)
print(items)