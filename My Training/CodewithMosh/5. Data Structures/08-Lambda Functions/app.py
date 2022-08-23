# Lambda Function
# lambda = anonymous function
# from ast import Expression


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# def sort_item(items):
#     return items[1]

# items.sort(key = sort_item, reverse=True)
# print(items)

# cleaner code
# items.sort(key=lambda parameters:Expression)
items.sort(key=lambda item:item[1])
print(items)

