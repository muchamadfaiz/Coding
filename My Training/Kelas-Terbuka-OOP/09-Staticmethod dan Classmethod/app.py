# Staticmethod dan Classmethod

class Hero:

    # private class variable
    __jumlah = 0

    def __init__(self, name):
        self.name = name
        Hero.__jumlah += 1

    # method ini hanya berlaku untuk objek
    def getJumlah(self):
        return Hero.__jumlah

    # method tidak berlaku untuk objek tapi berlaku untuk class
    def getJumlah1():
        return Hero.__jumlah

    # method static (decorator) nempel ke objek dan class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah


sniper = Hero("sniper")
print(sniper.getJumlah())  # method ini hanya berlaku untuk objek
print(Hero.getJumlah1())  # tidak berlaku pada class
print(Hero.getJumlah2())  # berlaku pada class dan objek

rikimaru = Hero("rikimaru")
print(Hero.getJumlah2())  # berlaku pada class dan objek
traxex = Hero("traxex")
print(rikimaru.getJumlah2())  # berlaku pada class dan objek
traxex = Hero("pawpaw")
print(rikimaru.getJumlah3())  # berlaku pada class dan objek
