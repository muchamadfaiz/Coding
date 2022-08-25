# Latihan Enkapsulasi

class Hero:
    # private class variable
    __jumlah = 0

    def __init__(self, name, health, attPower, armor):
        self.__name = name
        self.__baseHealth = health
        self.__baseAttPower = attPower
        self.__baseArmor = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__baseHealth * self.__level
        self.__attPower = self.__baseAttPower * self.__level
        self.__armor = self.__baseArmor * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} level {} : \n\thealth = {}/{}\n\tattack = {}\n\tarmor = {}".format(self.__name, self.__level, self.__health, self.__healthMax, self.__attPower, self.__armor)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name, "level up")
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__baseHealth * self.__level
            self.__attPower = self.__baseAttPower * self.__level
            self.__armor = self.__baseArmor * self.__level

    def attack(self, musuh):
        self.gainExp = 50


slardar = Hero("slardar", 100, 5, 10)
print(slardar.info)

# slardar.gainExp = 50 #sebelum pake def attack tidak otomatis dapat exp
# slardar.gainExp = 80 #sebelum pake def attack tidak otomatis dapat exp
# print(slardar.__dict__)
slardar.attack("axe")
slardar.attack("axe")
slardar.attack("axe")
slardar.attack("axe")
slardar.attack("axe")
print(slardar.__dict__)
print(slardar.info)
