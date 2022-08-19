# looping dari list

# for loop
print("For Loop")
kumpulan_angka = [1,4,5,2,2,3,5,1]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["Faiz", "Umiw", "pawpaw"]

for nama in peserta:
    print(f"nama = {nama}")

# for loop dan range
print("\nLoop and Range")

kumpulan_angka = [1,4,5,3,2,2,4]

panjang = len(kumpulan_angka)
for angka in range(panjang):
    print(f"angka = {kumpulan_angka[angka]}")

# While
print("While")
kumpulan_angka = [1,4,5,3,2,2,4]
panjang = len(kumpulan_angka)
count = 0

while count < panjang:
    print(f"angka = {kumpulan_angka[count]}")
    count += 1
    print(count)

# list comprehension
print("list comprehension")
data = ["ucup",1,2,3, "otong"]

[print(f"angka = {i}") for i in data]

# enumerate 
print("\nEnumerate")
data = ["ucup",1,2,3, "otong"]

for index,data in enumerate(data):
    print(f"index = {index}, data = {data}")

