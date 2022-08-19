# 1. using while varian 1
# sisi = int(input("masukan angka= "))
# angka = 0

# while angka < sisi:
#     angka += 1
#     print(angka * "*")
# print("akhir dari while varian 1")

# 2. using while varian 2
# sisi = int(input("masukan angka= "))
# angka = 0

# while True:
#     angka += 1
#     print(angka * "*")
#     if angka == sisi:
#         break
# print("akhir dari while varian 2")

# 3. using for
# sisi = 10
# angka2 = range(sisi)
# count = 1
# for i in angka2:
#     print("*" * count)
#     count += 1

# 4. Hanya ganjil saja

# sisi = int(input("berikan angka= "))

# angka = 0
# spasi = sisi // 2
# while angka < sisi:
#     angka += 1
#     # print jika ganjil
#     if angka % 2 != 0:
#         print(" " * spasi, "x" * angka, f"ini ganjil {angka}")
#         spasi -= 1

# print("akhir dari program")

# 5. mencoba buat pola ketupat

# sisi = int(input("berikan jumlah sisi= "))

# angka = 0
# spasi = sisi // 2
# while angka < sisi:
#     print (angka < sisi)
#     angka += 1
#     print(spasi * " ", angka * "+")
# while angka == 5:
#     angka -= 1
#     print(spasi * " ", angka * "+")

    
# print(angka < sisi)
# print("akhir dari program")

# 6. Percobaan ke-2 membuat pola ketupat (for)

# row = int(input("masukan jumlah baris = "))
# print("\n")

# for i in range (row):
#     print(row)
#     print(i)
#     print(row-i)
#     # print(f"baris ke {i}, {row-i}")
#     print(f"baris ke {i+1}"+" "*(row-i)+" *"*(i+1))

# print(f"akhir dari baris {i}")
# for j in range (row-1) :
#     print(row)
#     print(j)
#     print(row-j)
# # for j in range (row-1) :
#     # print(row-1)
#     print(f"baris ke {i-j}"+" " * (j+2) + " *" * (row-1-j))
# print(f"akhir dari baris {j}")

# 7. Percobaan ke-3 membuat pola ketupat (while)

# row = int(input("masukan angka = "))
# count = 0

# while count < row:
#     count += 1
#     print(row-1)
#     print(count)
#     print(" "*(row-count) + " S" * count)
#     if count == 3:
#         print("pawpaw")
#     if count == 4:
#         print("bilbil")
#     # if count == row:
#     #     # print(count)
#     # while count == row:
#     #     count -= 1
#     #     print(count)
#     #     print("faiz")
#     #     if count == 1:
#     #         break

# 8. percobaan ke-4 membuat pola ketupat (referensi youtube)

baris = int(input("masukan angka = "))

for i in range (baris):
    spasi = baris - i - 1
    print(spasi)
    star = i + 1
    print(star)
    print(" " * spasi + (" " + "S") * star)
print(star)
print(spasi)
for i in range (baris-1):
    spasi = i + 1
    print(spasi)
    star = baris - i - 1
    print(star)
    print(" " * spasi + (" " + "S") * star)
print(star)
print(spasi)