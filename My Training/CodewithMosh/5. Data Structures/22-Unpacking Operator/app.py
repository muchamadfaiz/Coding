# numbers = [1, 2, 3]
# print(*numbers)
# print(1, 2, 3)

# # values = list(range(5))
# values = [*range(5), "*Hello"]
# print(values)

# first = [1, 2]
# second = [3]
# # values = [*first, "a", *second, *"Hello"]
# values = [first, second]
# print(values)

first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 10}
print(combined)