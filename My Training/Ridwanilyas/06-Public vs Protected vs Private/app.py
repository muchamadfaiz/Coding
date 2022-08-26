"""
dalam accessing variabel terbagi 3 jenis
1. Public = bebas akses
2. Protected = hanya bisa diakses dalam kelas dan turunan
3. Private = hanya bisa diakses dalam kelas

"""


class Mahasiswa:
    # property class/static variabel
    JumlahMahasiswa = 0

    def __init__(self, nama, nim, ipk):
        # public
        self.nama = nama

        # protected
        self._nim = nim

        # private
        self.__ipk = ipk

        Mahasiswa.JumlahMahasiswa += 1


faiz = Mahasiswa("Muchamad Faiz", 23213123, 3.5)
# print(faiz.nama)
# faiz.nama = "MUCHAMAD FAIZ"
# print(faiz.nama)

# print(faiz._nim)
# faiz._nim = 242421123
# print(faiz._nim)

faiz.__ipk = 3
print(faiz.__ipk)
print(dir(faiz))
