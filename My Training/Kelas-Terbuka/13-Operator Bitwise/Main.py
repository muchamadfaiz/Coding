# Operator Bitwise, operasi biner (untuk tambahan mungkin nanti butuh)
# Operator Bitwise merupakan operasi masing2 bit

a = 9
b = 5

# bitwise OR (|)
c = a | b
d = format(a,'08b')
print("\n", "="*8,"OR", "="*8)
print("nilai :", a ,",", 'binary :', d)
print("nilai :", b ,",", 'binary :', format(b,'08b'))
print("-"*20, "(|)")
print("nilai :", c ,",", 'binary :', format(c,'08b'))

# bitwise AND (&)
c = a & b
print("\n", "="*8,"AND", "="*8)
print("nilai :", a ,",", 'binary :', d)
print("nilai :", b ,",", 'binary :', format(b,'08b'))
print("-"*20, "(&)")
print("nilai :", c ,",", 'binary :', format(c,'08b'))

# bitwise XOR (^)
c = a ^ b
print("\n", "="*8,"XOR", "="*8)
print("nilai :", a ,",", 'binary :', d)
print("nilai :", b ,",", 'binary :', format(b,'08b'))
print("-"*20, "(^)")
print("nilai :", c ,",", 'binary :', format(c,'08b'))

# bitwise NOT (~)
c = ~a
print("\n", "="*8,"NOT", "="*8)
print("nilai :", a ,",", 'binary :', d)
print("-"*20, "(~)")
print("nilai :", c ,",", 'binary :', format(c,'08b'))
print("-"*20, "(^)")
e = 0b0000001001 #ketika pake operasi ^ dua buah elemen harus sama tipenya (tidak bisa pake str atau int)
f = 0b1111111111
print("nilai :", f^e ,",", "binary :", format(f^e,'08b'))

# shifting

# shift right (>>)
c = a >> 2
print("\n", "="*8,">>", "="*8)
print("nilai :", a ,",", 'binary :', d)
print("-"*20, "(>>)")
print("nilai :", c ,",", 'binary :', format(c,'08b'))

# shift left (>>)
c = a << 2
print("\n", "="*8,"<<", "="*8)
print("nilai :", a ,",", 'binary :', d)
print("-"*20, "(<<)")
print("nilai :", c ,",", 'binary :', format(c,'08b'))