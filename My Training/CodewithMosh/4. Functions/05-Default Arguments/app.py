def increment(number, by):
    return number + by


print(increment(2, by=1))

# cleaner code using default arguments
def increment(number, by=1): #default argument comes after the required parameter
    return number + by


print(increment(2,7))

def increment(number,another, by=1): #default argument comes after the required parameter
    return number * another + by 


print(increment(5,2))