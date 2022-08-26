class Mahasiswa:
    def __init__(self):
        pass


faiz = Mahasiswa()

faiz.nama = "Muchamad Faiz"
faiz.ipk = 3.8
faiz.ip = [3.0, 3.5]
print(faiz.nama)
print(type(faiz.nama))
print(faiz.ipk)
print(type(faiz.ipk))
print(faiz.ip)
print(type(faiz.ip))

# kesimpulan klo dengan seperti di atas konsep OOP nya tidak ada,
# karena bisa menambahkan properti di luar class
