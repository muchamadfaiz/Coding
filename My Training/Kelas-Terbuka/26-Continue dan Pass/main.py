# continue, pass, break

# pass -> dia berfungsi sebagai dummy, tidak akan dieksekusi 

# angka = 0

# while angka < 5:
#     angka += 1

#     if angka == 3:
#         # print(f"ini loop nomor ke {angka} ")
#         pass

#     print(angka)

# continue

angka = 0

print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") # aksi 1

    if angka == 3:
        print("nize!")
        continue # akan membuat loop meloncat ke aksi setelahnya

    print("Faiz") # aksi 2
print("Finish")