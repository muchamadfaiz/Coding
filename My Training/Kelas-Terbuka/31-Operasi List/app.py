
data_angka = [1,2,34,5,6,2,1,4,4]

print(f"data angka = {data_angka}")

# count data 
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data (index)
#index     0       1         2        3   
data = ["ucup", "Otong", "Dudung", "ujang"]
print(f"data = {data}")

index_dudung = data.index("Dudung")
print(f"index si Dudung = {index_dudung}")

index_ujang = data.index("ujang")
print(f"index si Dudung = {index_ujang}")

# mengurutkan list
print(f"data angka sebelum sort = {data_angka}")
sort = data_angka.sort()
print(f"data angka sort = {data_angka}")

print(f"data sebelum sort = {data}")
sort = data.sort()
print(f"data angka sort = {data}")

# balik listnya
data_angka.reverse()
data.reverse()
print(f"data reverse\n{data_angka}\n{data}")
