# Enkapsulasi
# mengurangi bug
"""
syarat enkapsulasi
- buat semua variabel private
- getter = mengambil data/variabel yang dibutuhkan
- setter = mensetting data/variabel yang dibutuhkan
"""


class Hero:

    def __init__(self, name, health, attackPower):
        self.__name = name
        self.__health = health
        self.__attpower = attackPower

    # getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    def getattpower(self):
        return self.__attpower

    # setter

    def diserang(self, attackedPower):
        self.__health -= attackedPower

    def setAttPower(self, nilaibaru):
        self.__attpower = nilaibaru


# awal dari game
earthshaker = Hero("earthshaker", 50, 5)

print(earthshaker.__dict__)

# game berjalan
print(earthshaker.getName())
print(earthshaker.getHealth())
earthshaker.diserang(5)
print(earthshaker.getHealth())
earthshaker.setAttPower(100)
print(earthshaker.getattpower())
earthshaker.diserang(5)
print(earthshaker.getHealth())
