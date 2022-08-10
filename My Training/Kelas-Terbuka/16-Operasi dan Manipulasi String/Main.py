# Operasi dan manipulasi string

#1. menyambung string
nama_pertama = "ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_pertama +" " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

#2. Menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " =" , panjang)

#3. Operator untuk string

#mengecek apakah ada komponen char atau string di string
d = "d"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

d = "D"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap
print(d + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(10*"wk")

# indexing
print("index ke-0 : " +nama_lengkap[0])
print("index ke-0 : " +nama_lengkap[1])
print("index ke-0 : " +nama_lengkap[4])
print("index ke-0 : " +nama_lengkap[5])
print("index ke-0 : " +nama_lengkap[10])
print("index ke-0 : " +nama_lengkap[-1])
print("index ke-0 : " +nama_lengkap[-2])


