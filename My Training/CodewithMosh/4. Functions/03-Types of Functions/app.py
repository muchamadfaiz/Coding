"""
There is 2 types of function
1. Perform a task
2. Return a value
"""

# Perform Task
def greet (name):
    print(f"Hi {name}") # task is printing something on terminal


greet("Faiz")
# Return a value
round = round(1.9) # Return a value after it rounded
print(round)

# Return a value
def get_greeting (name):
    return f"Hi {name}"


message = get_greeting("Faiz")
file = open("content.txt", "w")
file.write(message)

# print(message)