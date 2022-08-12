# format string


# yang susah
from msilib.schema import Binary, ODBCTranslator


nama = "marlene"
str = "hello" + nama + "apa kabar" + "hai kamu"

print(str)

# contoh generic
# string
nama = "faiz"
format_str = f"halo {nama}, kamu lagi apa?"

print(format_str)

#boolean
boolean = True
format_str = f"bolean = {boolean}"
print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
angkaribu = 2000
angkajuta = 2000000
format_strribu = f"ribuan = {angkaribu:,}"
format_strjuta = f"jutaan = {angkajuta:,}"
print(format_strribu)
print(format_strjuta)

# bilangan desimal
angka = 2005.54321 
format_str = f"desimal = {angka:.2f}"
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:020.3f}"
print(format_str)

# menampilkan tanda + atau minus
angka_minus = -10
angka_plus = 10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika di dalam place holder
harga = 10000
jumlah = 5

format_string = f"harga total = Rp. {harga * jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)

angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)

