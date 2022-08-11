# operator dalam bentuk methods

## merubah case dari string

# merubah semua ke uppercase

salam = "bro"
print("normal =", salam)
salam = salam.upper()
print("upper =", salam)

# merubah semua ke lowercase
# bisa pake .lower
alay = "aKu keCe AbiezZZZ"
print("normal =", alay)
alay = alay.lower()
print("lower =", alay)

# bisa pake .casefold()
alay = "aKu keCe AbiezZZZ"
print("normal =", alay)
alay = alay.casefold()
print("lower =", alay)

## pengecekan dengan menggunakan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() #hasilnya bool
print(salam, "is lower =", apakah_lower)
apakah_upper = salam.isupper() #hasilnya bool
print(salam, "is upper =", apakah_upper)

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, newline \n
# istitle() <-- semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Orkay" #huruf awal harus besar semua utnuk dapet nilai True
cek_judul = judul.istitle()
print(judul, "is title =", cek_judul)

## ngecek komponen startswith() endswith() <-- keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim") #uppercase dll hrus sama untuk dapat nilai True
print("start = ", cek_start)

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = ", cek_end)

## penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabungan = " ".join(pisah)
print(pisah)
print(gabungan)

gabungan = " ehm ".join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))

# alokasi karakter rjust(), ljust(), center()

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,"m") #string.rjust(length, character)
print("'"+tengah+"'")

# kebalikannya -> strip()
tengah = kanan.strip()
print("'"+tengah+"'")









