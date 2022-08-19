# Operasi
# index  0(-4) 1(-3)  2(-2)   3(-1)
data = ["faiz", "umi", "pawpaw", "bilbil"]

# mengambil data data list diatas
# data_0 = data[0]
# print(f"data pertama index (index 0) = {data_0}")

# data_terakhir = data[-1]
# print(f"data terakhir index (index -1) = {data_terakhir}")

# data_faiz = data[-4]
# print(f"data faiz (index -4) = {data_faiz}")

# mengambil info jumlah data dalam list
# panjang_data = len(data)
# print(f"panjang data = {panjang_data}")

## Manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = {data}")
data.insert(1, "sinackal")
print(f"data sesudah ditambah = {data}")

# menambahkan di akhir list
data.append("debay")
print(f"data sesudah ditambah = {data}")

# menambahkan list dengan list
data_baru = ["gemoy", "bulbul"]
data.extend(data_baru)
print(f"data gabungan = {data}")

# merubah data
# kita ubah data 2 menjadi michael
data[2] = "michael"
print(f"data rubah = {data}")

# meremove data
data.remove("gemoy")
print(f"data remove = {data}")

# meremove data paling belakang
data.pop()
print(f"data remove2 = {data}")

