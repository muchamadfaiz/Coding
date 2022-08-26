class Mahasiswa:
    def __init__(self, nama, nim, ipk):
        self.__nama = nama
        self.__nim = nim
        self.__ipk = ipk

    @property  # dengan menggunakan method ini artinya method ini berperilaku sbg properti
    def info(self):
        print("nama : {}\nnim : {}\nipk : {}".format(
            self.__nama,
            self.__nim,
            self.__ipk
        )
        )


faiz = Mahasiswa("Muchamad Faiz", 2102012031, 3.9)
faiz.info  # jadi ga usah pake kurung buka kurung tutup
