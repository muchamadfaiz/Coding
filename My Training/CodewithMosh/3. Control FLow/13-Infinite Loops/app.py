# command = ""
# while command.lower() != "quit":
#     command = input (">")
#     print("ECHO", command)

while True:
    command = input (">")
    if command.lower() == "quit":
        break
    print("ECHO", command)
