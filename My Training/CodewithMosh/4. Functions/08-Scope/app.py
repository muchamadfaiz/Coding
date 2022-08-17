"""
Variable
1. Local Variable
2. Globa Variable

#do not modify variable on function into global variable using "global"
"""

def greet(name):
    message = f"Hi {name}" # message is the example of local variable
    return message

message = "contoh global variabel" # message here is the example of global variable
def send_email(name):
    pass


print(greet("Faiz"))
print(message)
