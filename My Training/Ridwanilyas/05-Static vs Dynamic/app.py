class Mahasiswa():
    # class property/varibel class/attribut class
    JumlahMahasiswa = 0

    def __init__(self, nama, nim, ipk):
        # property instance/variabel instance/atttribut instance
        self.nama = nama
        self.nim = nim
        self.ipk = ipk
        Mahasiswa.JumlahMahasiswa = Mahasiswa.JumlahMahasiswa + 1


faiz = Mahasiswa("Muchamad Faiz", 123113323, 3.8)
umi = Mahasiswa("Herviana NUrulita", 214414211, 3.9)
# print(Mahasiswa.__dict__)
# help(Mahasiswa)
print(dir(faiz))
# print(faiz.__dict__)
print(Mahasiswa.JumlahMahasiswa)
print(faiz.JumlahMahasiswa)
