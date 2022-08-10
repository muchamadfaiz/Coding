# episode latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# ++++++3------10++++++
# kasus gabungan
#inputUser = float(input("masukan angka yang bernilai\nkurang dari 3 \natau \nlebih besar dari 10\n:"))

# ++++++3------------
# memeriksa angka kurang dari 3
#isKurangDari = inputUser < 3
#print('kurang dari 3 =',isKurangDari)

# ------------10++++++
# memeriksa angka lebih dari 10
#isLebihDari = inputUser > 10
#print('lebih dari 10 =',isLebihDari)

#isCorrect = isKurangDari or isLebihDari
#print("angka yang anda masukan =", isCorrect)

# ------3++++++10------
# kasus irisan

#print("\n","="*15,"\n")
#inputUser = float(input("masukan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari 10\n:"))

#------3++++++
# memeriksa angka lebih dari 3
#islebihDari = inputUser > 3
#print("lebih dari 3 =", islebihDari)

# ++++++10------
# memeriksa angka kurang dari 10
#isKurangDari = inputUser < 10
#print("kurang dari 10 =", isKurangDari)

#isCorrect = islebihDari and isKurangDari
#print("angka yang anda masukan =", isCorrect)

 #SOAL LATIHAN
print ("1. ------0++++++5------8++++++11------")
InputUser = float(input("masukan angka yang masuk range soal diatas:" ))

 memeriksa angka lebih dari 0
isLebihDari0 = InputUser > 0
print ("lebih dari 0:", isLebihDari0)

 memeriksa angka kurang dari 5
isKurangDari5 = InputUser < 5
print ("kurang dari 5:", isKurangDari5)

 memeriksa angka lebih dari 8
isLebihDari8 = InputUser > 8
print ("lebih dari 8:", isLebihDari8)

 memeriksa angka kurang dari 11
isKurangDari11 = InputUser < 11
print ("kurang dari 11:", isKurangDari11)

isCorrect = (isLebihDari0 and isKurangDari5) or (isLebihDari8 and isKurangDari11 )
print("angka yang anda masukan :", isCorrect)


print("2. ++++++0------5++++++8------11++++++")
inputUser = float(input("masukan angka yang masuk range diatas:"))

# memeriksa angka kurang dari 0
isKurangdari0 = inputUser < 0
print("kurang dari 0 :", isKurangdari0)

# memeriksa angka lebih dari 5
isLebihdari5 = inputUser > 5
print("lebih dari 5 :", isLebihdari5)

# memeriksa angka kurang dari 8
isKurangdari8 = inputUser < 8
print("kurang dari 8 :", isKurangdari8)

# memeriksa angka lebih dari 11
isLebihdari11 = inputUser > 11
print("lebih dari 11 :", isLebihdari11)

isCorrect = (isKurangdari0 or isLebihdari5) and (isKurangdari8 or isLebihdari11)
print("angka yang anda masukan", isCorrect)





