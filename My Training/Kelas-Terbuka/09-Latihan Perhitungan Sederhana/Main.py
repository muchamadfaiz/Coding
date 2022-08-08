# latihan konversi satuan

# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("masukan suhu dalam celcius: "))
print("suhu adalah", celcius, "C")

#Reamur
reamur = (4 / 5) * celcius
print ("suhu dalam reamur = ", reamur, "R")

#Fahrenheit
fahrenheit = (9 / 5) * celcius + 32
print ("suhu dalam fahrenheit = ", fahrenheit, "F")

#Kelvin
kelvin = celcius + 273
print ("suhu dalam kelvin = ", kelvin, "K\n")


reamur = float(input("masukan suhu dalam reamur: "))
print("suhu dalam reamur", reamur, "R")

#Celcius
celcius = (5 / 4) * reamur
print("suhu dalam celcius = ", celcius, "C")

#Fahrenheit
fahrenheit = (9 / 4) * reamur + 32
print("suhu dalam fahrenheit = ", fahrenheit, "F")

#Kelvin
celcius = (5 / 4) * reamur + 273
print("suhu dalam celcius = ", celcius, "C\n")


fahrenheit = float(input("masukan suhu dalam fahrenheit: "))
print("suhu dalam fahrenheit", fahrenheit, "F")

#Celcius
celcius = (5 / 9) * (fahrenheit - 32) 
print("suhu dalam celcius = ", celcius, "C")

#Reamur
reamur = (4 / 9) * (fahrenheit - 32)
print("suhu dalam fahrenheit = ", fahrenheit, "F")

#Kelvin
kelvin = (5 / 9) * (fahrenheit - 32) + 273
print("suhu dalam celcius = ", celcius, "C\n")

kelvin = float(input("masukan suhu dalam kelvin: "))
print("suhu dalam kelvin", kelvin, "F")

#Celcius
celcius = kelvin - 273
print("suhu dalam celcius = ", celcius, "C")

#Reamur
reamur = (9 / 5) * (kelvin - 273) + 32
print("suhu dalam fahrenheit = ", fahrenheit, "F")

#fahrenheit
kelvin = (5 / 9) * (fahrenheit - 32) + 273
print("suhu dalam celcius = ", celcius, "C")