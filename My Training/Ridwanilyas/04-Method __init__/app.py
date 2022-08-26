class Mahasiswa:
    # constructor = sebuah method yang dipanggil pertama kali saat objek
    #               dibuat (instantiasi objek)
    def __init__(self):
        print("mahasiswa berhasil dibuat")

    def sapa(self):
        print("halo saya mahasiswa")


faiz = Mahasiswa()
umi = Mahasiswa()

faiz.sapa()
umi.sapa()
