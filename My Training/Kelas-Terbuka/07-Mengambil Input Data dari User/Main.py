# Episode input user

#data yang dimasukan pasti string
data = input("masukan data: ")
print("data = ", data, ",type = ", type(data))

#jika kita ingin mengambil int, maka
angka = int(input("masukan angka: "))
angka = float(input("masukan angka: "))

print("data = ", angka, ",type = ", type(angka))

# bagaimana dengan boolean
biner = bool(int(input("masukan nilai bolean: ")))
print("data = ", biner, ",type = ", type(biner))
