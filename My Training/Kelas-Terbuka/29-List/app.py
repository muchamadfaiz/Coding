# LIST

# kumpulan data numbers
data_angka = [1, 2, 3]
print(data_angka)

# kumpulan data string
data_string = ["faiz, pawpaw, bilbil, umiw"]
print(data_string)

# kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# kumpulan data campuran
data_campuran = [1, "ucup", True, 2, 3, True]
print(data_campuran)

# cara alternatif membuat list
data_range = range(0,10, 2) # range (start, stop, step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
# list = [expression for item in iterable]
angka = range(0,10)
data_list = list(angka)
print(data_list)

list_pake_for = [i for i in range(0, 10)]
print(list_pake_for)

list_pake_for = [i for i in "faiz"]
print(list_pake_for)

list_pake_for = [i**2 for i in range(0, 10)]
print(list_pake_for)

# membuat list pake for pake if
# newlist = [expression for item in iterable if condition == True]
list_pake_for_if_genap = [i for i in range(0,10) if i % 2 == 0]
print(list_pake_for_if_genap)

list_pake_for_if_ganjil = [i for i in range(0,10) if i % 2 != 0]
print(list_pake_for_if_ganjil)