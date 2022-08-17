def increment(number, by):
    return number + by


result = increment(2,1)
print(result)

# Cleaner code with keyword argument
def increment(number, by):
    return number + by


print(increment(number=2,by=1)) #by=1 & number=2 is keyword argument

