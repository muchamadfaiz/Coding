from os import stat


class Mahasiswa:
    __JumlahMahasiswa = 0

    def __init__(self, nama, nim, ipk):
        self.nama = nama
        self.nim = nim
        self.ipk = ipk
        Mahasiswa.__JumlahMahasiswa += 1

    @staticmethod
    def tampil():
        print(Mahasiswa.__JumlahMahasiswa)


faiz = Mahasiswa("Muchamad Faiz", 231231231, 3.9)
# print(dir(faiz))
# print(Mahasiswa.__JumlahMahasiswa) # ga bisa di akses
# print(Mahasiswa._Mahasiswa__JumlahMahasiswa) # bisa coba liat dir nya
Mahasiswa.tampil()  # bisa karena memang dikhususkan untuk class
faiz.tampil()  # harusnya ga bisa
