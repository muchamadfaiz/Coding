# Everything in python is an object
# Fungsi Class juga objek
# class adalah sebuah objek untuk membuat objek baru
# class is mappingproxy

class Mahasiswa:
    #     pass
    # {'__module__': '__main__',
    # '__dict__': <attribute '__dict__' of 'Mahasiswa' objects>,
    # '__weakref__': <attribute '__weakref__' of 'Mahasiswa' objects>,
    #  '__doc__': None}
    # print(Mahasiswa.__dict__)
    """doc for Mahasiswa"""

    a = 10


# 1. melihat class dictionary (__dict__)
print("=" * 8, "class dict", "=" * 8)
# memperlihatkan mappingproxy dalam bentuk dictionary dan read only
print(Mahasiswa.__dict__)
print(Mahasiswa.__dict__["a"])  # mengakses data pada key = "faiz"

# ga bisa melakukan ini (akan muncul typeErrorException) karna hanya read only harus lewat classnya
# Mahasiswa.__dict__["a"] = 100

# 2. melihat doc string attribute (__doc__)
print("=" * 8, "doc string", "=" * 8)
print(Mahasiswa.__doc__)  # mengakses data pada key = __doc__
# 3. melihat name string attribute (__name__)

print(Mahasiswa.__name__)  # mengakses data pada key = __name__
# 4. dot (.) syntax untuk mengakses (mengassign atau mengambil) atribut dari kelas atau objek
print("=" * 8, "dot syntax", "=" * 8)
Mahasiswa.b = 20  # contoh assign data
print(Mahasiswa.__dict__)
# classes that wrintten in C language like "str", "int" weill be with lowercase letter

# 5. getattr() untuk mengakses data
print("=" * 8, "mengambil data", "=" * 8)
print(getattr(Mahasiswa, "b"))  # sama kayak pake dot syntax
# print(getattr(Mahasiswa, "pawpaw"))  # ga bisa melakukan ini (akan muncul attributeError) karna tidak ada atribute pawpaw di objek tsb
# tapi bisa ga eror kalo masukin data di argumen ke tiga
print(getattr(Mahasiswa, "d", "salah lu"))

# 5. setattr() untuk mengasign data
print("=" * 8, "set atribut", "=" * 8)
# sama seperti Mahasiswa.kucing = "pawpaw"
setattr(Mahasiswa, "d", 40)
print(Mahasiswa.__dict__)

# 6. delattr() untuk delete data
print("=" * 8, "delete atribut", "=" * 8)
delattr(Mahasiswa, "d")  # sama seperti del Mahasiswa.kucing
print(Mahasiswa.__dict__)

# 7.Instance Dictionary
# tidak seperti class an object __dict__ hanya sebuah dictionary biasa bukan mappingproxy
print("=" * 8, "instance dictionary", "=" * 8)
faiz = Mahasiswa()
faiz.b = 20  # assign data ke objek faiz
print(faiz.__dict__)
print(faiz.a)  # sama seperti getattr(faiz,"a")
# bisa dilakukan karena tidak seperti class yang read only
faiz.__dict__["c"] = 30
print(faiz.__dict__)
print(faiz.c)  # sama seperti getattr(faiz,"a")

# 8. attribute lookup order (urutan pencarian atribut)
# kamu dapat mengakses atribut class menggunakan objek
print(faiz.b)
# bisa mengasign data baru
faiz.a = 100
print(faiz.a)
print(faiz.__dict__)
# tapi klo lihat di class atribute tidak ada yg berubah a = 10
print(Mahasiswa.a)
# class atribute di share ke semua objek turunanny
umi = Mahasiswa()
print(umi.a)
