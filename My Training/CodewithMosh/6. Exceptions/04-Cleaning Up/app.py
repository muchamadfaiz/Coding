try:
    open("app.py")
    age = int(input("age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age.")
else:
    print("No exception was thrown")
finally:
    file.close()
    
