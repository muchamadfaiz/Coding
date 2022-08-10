# Operasi dan manipulasi string

#1. menyambung string
from tarfile import LENGTH_LINK


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
print("index ke-1 : " +nama_lengkap[1])
print("index ke-4 : " +nama_lengkap[4])
print("index ke-5 : " +nama_lengkap[5])
print("index ke-10 : " +nama_lengkap[10])
print("index ke -1: " +nama_lengkap[-1])
print("index ke-2: " +nama_lengkap[-2])
print("index ke-[0:3]: " +nama_lengkap[0:3]) # : artinya sampai
print("index ke-[3:8]: " +nama_lengkap[3:8]) # : artinya sampai
print("index ke-[0,2,4,6,8,10]: " +nama_lengkap[0:10:2]) # : artinya 0 sampai 10 dengan increment 2

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling besar
print("paling bear : " + max(nama_lengkap))

ascii_code = ord(" ")
print ("ASCII code untuk spasi adalah ",ascii_code)
ascii_code = ord("'")
print ("ASCII code untuk spasi adalah ",ascii_code)
data = 117
print("char untuk ASCII 117 adalah", chr(data))

# 4. Operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada data =", jumlah)

