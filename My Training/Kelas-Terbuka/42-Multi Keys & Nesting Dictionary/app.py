import datetime as dat
from re import X
from socket import NI_MAXHOST

mahasiswa1 = {
    "nama" : "muchamad faiz",
    "NIM" : "12321422123",
    "sks_lulus" : 350,
    "is_beasiswa" : False,
    "lahir" : dat.datetime(2001,4,10)
}
mahasiswa2 = {
    "nama" : "pawpaw",
    "NIM" : "12323243242123",
    "sks_lulus" : 323,
    "is_beasiswa" : False,
    "lahir" : dat.datetime(1993,4,10)
}

mahasiswa3 = {
    "nama" : "bilbil",
    "NIM" : "12321422123",
    "sks_lulus" : 350,
    "is_beasiswa" : True,
    "lahir" : dat.datetime(1987,4,10)
}

data_mahasiswa = {
    "MAH001" : mahasiswa1,
    "MAH002" : mahasiswa2,
    "MAH003" : mahasiswa3,
}

print(f"{'KEY':<6} {'NAMA':<17} {'SKS':<3} {'Beasiswa':<9} {'lahir':<10}")
print("-"*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]["nama"]
    NIM = data_mahasiswa[KEY]["NIM"]
    SKS = data_mahasiswa[KEY]["sks_lulus"]
    BEASISWA = data_mahasiswa[KEY]["is_beasiswa"]
    LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")

    print(f"{KEY:<6} {NAMA:<17} {SKS :<3} {BEASISWA :^9} {LAHIR:<10}")

