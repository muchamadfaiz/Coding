# Kenapa OOP

"""
1. Class (Template)
- property
- method (f(x))

2. Object
- instantiasi dari sebuah class

ex:
Class = mahasiswa
properti = nama,nim, ipk
method = tampilidentitas(), hitungipk()

parameter self itu menuju ke objeknya
"""


class Mahasiswa:
    # constructor
    def __init__(self, nama, nim):
        # property
        self.nama = nama
        self.nim = nim
    # method

    def sapa(self):  # self harus ada utuk menandakan method itu punyanya si objek
        print("hai {}".format(self.nama))


# instantiasi objek
faiz = Mahasiswa("muchamad faiz", 1201203123)
# print(dir(faiz))
# print(faiz.__dict__)
# help(faiz)
faiz.sapa()
# bisa langsung panggil propertiesnya
print(faiz.nama)
print(faiz.nim)
