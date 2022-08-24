# Game Sederhana (Saling Serang)
class Hero:
    def __init__(self, inputName, inputHealth, inputAttackPower, inputDeffence):
        self.name = inputName
        self.health = inputHealth
        self.attack = inputAttackPower
        self.deffence = inputDeffence

    def doattack(self, vilain):
        print(f"{self.name} menyerang {vilain.name}")
        vilain.dodefend(self, self.attack)

    def dodefend(self, vilain, attackPower_lawan):
        print(f"{self.name} diserang {vilain.name}")
        attack_diterima = attackPower_lawan/self.deffence
        print(f"serangan terasa {int(attack_diterima)}")
        self.health -= attack_diterima
        print(f"darah tersisa {int(self.health)}")


sniper = Hero("sniper", 100, 200, 3)
rikimaru = Hero("rikimaru", 100, 250, 10)

sniper.doattack(rikimaru)
print("\n")
rikimaru.doattack(sniper)
