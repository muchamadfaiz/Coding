# Teknik menduplikat list

a = ["Ucup", "Otong", "Dudung"]
print(f"a = {a}")

b = a 
print(f"b = {b}")

# kita akan merubah member dari a

# ini akan merubah kedua list
a[1] = "Pawpaw"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address a = {hex(id(b))}")

# menduplikat list dengan copy
c = a.copy()
print(f"address c = {hex(id(c))}")
print(c)
c[0] = "gemoy"
print(c)
