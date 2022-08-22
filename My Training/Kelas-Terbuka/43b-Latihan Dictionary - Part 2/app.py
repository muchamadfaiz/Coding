import datetime as dat
import os
import string
import random

# template dict mahasiswa
mahasiswa_template = {
    "nama":"nama",
    "nim":"00000000",
    "lahir":dat.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
    # os.system("cls") --> clear terminal
    os.system("cls")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    # print(mahasiswa)
    mahasiswa['nama'] = input("Nama Mahasiswa:")
    mahasiswa['NIM'] = input("NIM Mahasiswa:")
    mahasiswa['sks_lulus'] = int(input("SKS Lulus:"))
    TAHUN_LAHIR = int(input("Tahun Lahir (YYYY):"))
    BULAN_LAHIR = int(input("Bulan Lahir (1-12):"))
    TANGGAL_LAHIR = int(input("Tanggal Lahir (1-30):"))
    mahasiswa['lahir'] = dat.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    print(f"{'KEY':<6} {'NAMA':<17} {'NIM':<3} {'SKS':<3} {'lahir':<10}")
    print('-'*60)


    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]["nama"]
        NIM = data_mahasiswa[KEY]["NIM"]
        SKS = data_mahasiswa[KEY]["sks_lulus"]
        LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")

        print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS :<10} {LAHIR:<10}")

    print("y/n")
    is_done = input("apakah sudah selesai (y/n) ")
    if is_done == "y":
        break

print("\nakhir dar program")    