"""
Exercise 
time = 10 -15 minutes
def fizz_buzz(input):

if input divisible by 3 --> Fizz
if input divisible by 5 --> Buzz
if input divisible by 3 or 5 --> FizzBuzz
if input divisible by other --> input


"""

# percobaan pertama
# def fizz_buzz(input):
#     if input == 3:
#         b = "Fizz"
#         return b
#     elif input == 5:
#         c = "Buzz"
#     elif input == 3*5:
#         c = "FizzBuzz"
#         return c
#     else:
#         return input
# pass

# print(fizz_buzz(15))

# percobaan kedua
# def fizz_buzz(input):
#     if input % 3 == 0:
#         return "Fizz"
#     elif input % 5 == 0:
#         return "Buzz"
#     elif input % 3 and input % 5:
#         return "FizzBuzz"
#     else:
#         return input

# print(fizz_buzz(15))

# # percobaan ketiga
# def fizz_buzz(input):
#     if input % 3 == 0:
#         hasil = "Fizz"
#     elif input % 5 == 0:
#         hasil = "Buzz"
#     elif input % 3 and input % 5:
#         hasil = "FizzBuzz"
#     else:
#         hasil = input
#     return hasil

# print(fizz_buzz(25))

# percobaan keempat
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 ==0):
        return "FizzBuzz"    
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(7))
