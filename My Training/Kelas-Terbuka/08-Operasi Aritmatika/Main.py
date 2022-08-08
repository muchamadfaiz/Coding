#operasi aritmatika

a = 10
b = 3

# operasi tambah +
hasil = a + b
print (a, "+", b , "=", hasil)

# operasi tambah -
hasil = a - b
print (a, "-", b , "=", hasil)

# operasi perkalian *
hasil = a * b
print (a, "*", b , "=", hasil)

# operasi pembagian /
hasil = a / b
print (a, "/", b , "=", hasil)

# operasi eksponen **
hasil = a ** b
print (a, "**", b , "=", hasil)

# operasi modulus %
hasil = a % b
print (a, "%", b , "=", hasil)

# operasi modulus //
hasil = a // b
print (a, "//", b , "=", hasil)

# Prioritas operasi, operational precedence
"""
    1. ()
    2. exponen **
    3. Perkalian dan teman teman * / % //
    4. Pertambahan dan pengurangan + -
"""
x = 3
y = 2
z = 4

# yang duluan (),exponen, perkalian, pertambahan
hasil = x ** y * z + x / y - y % z // x
print(x,"**",y,"*",z,"+",x,"/",y,"-",y,"%",z,"//",x, "=", hasil)

hasil = x + y * z
print(x,"+",y,"*",z, "=", hasil)

hasil = (x + y) * z
print("(",x,"+",y,")", "*",z, "=", hasil)