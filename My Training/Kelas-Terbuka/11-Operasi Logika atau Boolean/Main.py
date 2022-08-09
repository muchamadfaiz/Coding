# Operasi logika atau boolean

# not, and, and, xor

# NOT
print('='*4, "NOT",'='*4 )
a = True
c = not a
print("data a =", a)
print("-"*10, "NOT")
print("data c =", c)

# OR (jika salah satu true makan hasilnya akan "True")
print('='*4, "OR",'='*4 )
a = False
b = False
c = a or b
print(a, "OR", b, "=", c)
a = False
b = True
c = a or b
print(a, "OR", b, "=", c)
a = True
b = False
c = a or b
print(a, "OR", b, "=", c)
a = True
b = True
c = a or b
print(a, "OR", b, "=", c)

# AND (jika dua buah nilai "True", maka hasilnya akan "True")
print('='*4, "AND",'='*4 )
a = False
b = False
c = a and b
print(a, "AND", b, "=", c)
a = False
b = True
c = a and b
print(a, "AND", b, "=", c)
a = True
b = False
c = a and b
print(a, "AND", b, "=", c)
a = True
b = True
c = a and b
print(a, "AND", b, "=", c)

# XOR (akan "True" jika dua buah nilai "True", sisanya "False")
print('='*4, "XOR",'='*4 )
a = False
b = False
c = a ^ b
print(a, "XOR", b, "=", c)
a = False
b = True
c = a ^ b
print(a, "XOR", b, "=", c)
a = True
b = False
c = a ^ b
print(a, "XOR", b, "=", c)
a = True
b = True
c = a ^ b
print(a, "XOR", b, "=", c)