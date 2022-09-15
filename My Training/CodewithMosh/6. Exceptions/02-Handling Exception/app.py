from ctypes.wintypes import tagMSG


try:
    age = int(input("age: "))
except ValueError as e:
    print("you didn't enter a valid age.")
    print(e)
    print(type(e))
else:
    print("No exception was thrown")
print("Execution Continues.")
