class Hero:  # template / blueprint for creating object
    # class variable
    jumlah = 0

    # akan di eksekusi saat si object di buat
    def __init__(self, inputName, inputPower, inputHealth, inputArmor):
        # print("hallo",x) # self adalah si hero1
        # instance variabel
        self.name = inputName
        self.power = inputPower
        self.health = inputHealth
        self.armor = inputArmor
        Hero.jumlah += 1
        print(f"membuat hero dengan nama {self.name}")


# hero1 = Hero(10) # hero1 --> object
hero1 = Hero("sniper", 100, 10, 4)  # hero1 --> object ke-1
print(Hero.jumlah)
hero2 = Hero("mirana", 100, 15, 1)  # hero1 --> object ke-2
print(Hero.jumlah)
hero3 = Hero("faiz", 1000, 100, 0)  # hero1 --> object ke-3, jadi ada 3 objek
print(Hero.jumlah)

print(hero1.__dict__)  # untuk melihat atrribut yang ada di objek tsb
print(hero1.name)
print(hero1.power)
print(hero1.health)
print(hero1.armor)

print(hero2.__dict__)  # untuk melihat atrribut yang ada di objek tsb
print(hero2.name)
print(hero2.power)
print(hero2.health)
print(hero2.armor)

print(hero3.__dict__)  # untuk melihat atrribut yang ada di objek tsb
print(hero3.name)
print(hero3.power)
print(hero3.health)
print(hero3.armor)

print(Hero.__dict__)
