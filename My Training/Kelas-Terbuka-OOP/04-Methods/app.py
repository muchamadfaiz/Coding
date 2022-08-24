class Hero:
    # class variable
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor) -> None:
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    # method tanpa return, tanpa argumen
    def siapa(self):
        print(f"namaku adalah {self.name}")

    # method dengan argumen
    def healthUp(self, up):
        self.health += up

    # method dengan return
    def getHealth(self):
        return self.health


hero1 = Hero("sniper", 100, 10, 5)
hero2 = Hero("faiz", 90, 5, 10)

hero1.siapa()

# print(hero1.__dict__)
# print(hero2.__dict__)

# method dengan argumen
hero1.healthUp(100)
print(hero1.health)

# method dengan return
print(hero1.getHealth())
