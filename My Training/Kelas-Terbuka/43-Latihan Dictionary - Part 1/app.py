import datetime as dat
import os

# template dict mahasiswa
mahasiswa_template = {
    "nama":"nama",
    "nim":"00000000",
    "lahir":dat.datetime(1111,1,11)
}

data_mahasiswa = {}

# os.system("cls") --> clear terminal
os.system("cls")
print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print("-"*20)

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
# print(mahasiswa)
mahasiswa['nama'] = input("Nama Mahasiswa:")
mahasiswa['nim'] = input("NIM Mahasiswa:")
mahasiswa['sks_lulus'] = int(input("SKS Lulus:"))
TAHUN_LAHIR = int(input("Tahun Lahir (YYYY):"))
BULAN_LAHIR = int(input("Bulan Lahir (1-12):"))
TANGGAL_LAHIR = int(input("Tanggal Lahir (1-30):"))
mahasiswa['lahir'] = dat.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
print(mahasiswa)
