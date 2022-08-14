# Kalkulator Sederhana

print("="*10)
print("Kalkulator Sederhana")
print("="*10,"\n")

angka_1 = float(input("Masukan angka_1: "))
angka_2 = float(input("Masukan angka_2: "))
operator = input("masukan operator (+,-,*,/): ")

if operator == "+":
    hasil = angka_1 + angka_2
    print (f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print (f"hasilnya adalah {hasil}")
elif operator == "*":
    hasil = angka_1 * angka_2
    print (f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print (f"hasilnya adalah {hasil}")
else:
    print("salah tuh")

print("akhir dari program")