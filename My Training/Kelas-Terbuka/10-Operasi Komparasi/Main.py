# operasi komparasi

# setiap hasil dari komparasi adalah boolean

'''
    1. > : lebih besar
    2. < : kurang dari
    3. >= : lebih dari sama dengan
    4. <= : kurang dari sama dengan
    5. == : sama dengan
    6. != : tidak sama dengan
    7. is
    8. is not
'''

a = 4
b = 2

# lebih besar dari >
print("="*4, "lebih besar dari (>)", "="*4)
hasil = a > 3
print (a, ">", 3, "=", hasil)
hasil = b > 3
print (b, ">", 3, "=", hasil)
hasil = b > 2
print (b, ">", 2, "=", hasil)

# kurang dari <
print("="*4, "kurang dari (<)", "="*4)
hasil = a < 3
print (a, "<", 3, "=", hasil)
hasil = b < 3
print (b, "<", 3, "=", hasil)
hasil = b < 2
print (b, "<", 2, "=", hasil)

# lebih dari sama dengan <
print("="*4, "lebih dari sama dengan (>=)", "="*4)
hasil = a >= 3
print (a, ">=", 3, "=", hasil)
hasil = b >= 3
print (b, ">=", 3, "=", hasil)
hasil = b >= 2
print (b, ">=", 2, "=", hasil)

# kurang dari sama dengan <
print("="*4, "kurang dari sama dengan (<=)", "="*4)
hasil = a <= 3
print (a, "<=", 3, "=", hasil)
hasil = b <= 3
print (b, "<=", 3, "=", hasil)
hasil = b <= 2
print (b, "<=", 2, "=", hasil)

# sama dengan ==
print("="*4, "sama dengan (==)", "="*4)
hasil = a == 3
print (a, "==", 3, "=", hasil)
hasil = b == 3
print (b, "==", 3, "=", hasil)
hasil = b == 2
print (b, "==", 2, "=", hasil)

# tidak sama dengan !=
print("="*4, "tidak sama dengan (!=)", "="*4)
hasil = a != 3
print (a, "!=", 3, "=", hasil)
hasil = b != 3
print (b, "!=", 3, "=", hasil)
hasil = b != 2
print (b, "!=", 2, "=", hasil)

# "is" sebagai komparasi object identity
x = 5 #ini adalah assignment membuat object
y = 5
print('nilai x =',x, "id = ", hex(id(x)))
print('nilai y =',x, "id = ", hex(id(x)))
hasil = x is y
print ('x is y =', hasil)

x = 5 #ini adalah assignment membuat object
y = 6
print('nilai x =',x, "id = ", hex(id(x)))
print('nilai y =',x, "id = ", hex(id(x)))
hasil = x is y
print ('x is y =', hasil)

# "is not" sebagai komparasi object identity
x = 5 #ini adalah assignment membuat object
y = 5
print('nilai x =',x, "id = ", hex(id(x)))
print('nilai y =',x, "id = ", hex(id(x)))
hasil = x is not y
print ('x is not y =', hasil)

# "is not" sebagai komparasi object identity
x = 5 #ini adalah assignment membuat object
y = 6
print('nilai x =',x, "id = ", hex(id(x)))
print('nilai y =',x, "id = ", hex(id(x)))
hasil = x is not y
print ('x is not y =', hasil)