# Date and tint(ime (latihan)

import datetime as dt

#Tanggal terserah sekarang
# hari_ini = dt.date.today()
# print(hari_ini)
# print(f"hari ini adalah hari = {hari_ini:%A}")
# print(f"hari ini adalah hari = {hari_ini:%a}")
# print(f"hari ini adalah hari = {hari_ini:%w}")

#Tanggal terserah kita
# tanggal = dt.date(2022,8,15)
# print(tanggal)
# print(f"hari ini adalah hari = {tanggal:%A}")

print("silahkan masukan tanggal, \nbulan dan tahun lahir anda\n")
tanggal = int(input("Tanggal \t:"))
bulan = int(input("Bulan \t\t:"))
tahun = int(input("Tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir:%d}")
print(f"Hari lahir anda adalah : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = umur_hari.days % 365 // 30
print(f"umur anda adalah :{umur_tahun} Tahun, {umur_bulan_sisa} Bulan")





