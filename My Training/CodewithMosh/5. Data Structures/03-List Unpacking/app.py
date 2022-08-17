# List Unpacking

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
# first, second, third = numbers #this is list unpacking
# first, second, *other = numbers #this is list unpacking
first, *other, last = numbers #this is list unpacking
print(f"data pertama = {first}")
print(f"data lain = {other}")
print(f"data terakhir = {last}")


# first = numbers[0]
# second = numbers[1]
# third = numbers[2]