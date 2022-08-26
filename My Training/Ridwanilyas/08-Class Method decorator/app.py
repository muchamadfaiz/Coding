class Mahasiswa:
    __jumlahMahasiswa = 0

    def __init__(self, nama, nim, ipk):
        self.nama = nama
        self.nim = nim
        self.ipk = ipk
        Mahasiswa.__jumlahMahasiswa += 1

    @staticmethod
    def tampil():
        return print(Mahasiswa.__jumlahMahasiswa)

    @classmethod
    # agar kita bisa mengakses kelasnya tanpa perlu menuliskan
    def tampilJumlahMahasiswa(cls):
        print(cls.__jumlahMahasiswa)


faiz = Mahasiswa("Muchamad Faiz", 23123133, 3.9)
# faiz.tampil()
# Mahasiswa.tampil()
faiz.tampilJumlahMahasiswa()
