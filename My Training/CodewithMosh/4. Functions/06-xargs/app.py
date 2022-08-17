def multiply(x, y):
    return x * y
pass


# multiply (1,2,3,4) # error because there is only 2 parameter

#For Solving the problem above we must replace those argument

def angka2 (*numbers):
    total = 1
    iterasi_ke = 0
    for number in numbers:
        iterasi_ke += 1
        total *= number
        print(f"ini iterasi ke-{iterasi_ke} = {total}")   
    return total
    

print(angka2(2, 3, 4, 5))

# (2, 3, 4, 5) = Touples --> parenthesis
# ([2, 3, 4, 5]) = Touples --> square bracket