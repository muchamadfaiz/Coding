# menggunakan fungsi super()
# agar lebih otomatis jika merubah nama class

# 1.  # tanpa fungsi super()


# class Hero:
#     def __init__(self, name, health):
#         self.nama = name
#         self.darah = health


# class HeroIntelligent(Hero):
#     def __init__(self, name):
#         self.nama = name  # ada perulangan disini
#         self.darah = 100  # ada perulangan disini


# class HeroStrength(Hero):
#     def __init__(self, name):
#         self.nama = name  # ada perulangan disini
#         self.darah = 200  # ada perulangan disini


# lina = HeroIntelligent("lina")
# axe = HeroStrength("axe")
# print(lina.nama, " ", lina.darah)
# print(axe.nama, " ", axe.darah)


# 2. dengan fungsi super()
from tkinter.messagebox import showinfo


class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print(f"{self.name} dengan darah: {self.health}")


class HeroIntelligent(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name, 100) # class Hero jika dirubah ini tidak otomatis berubah
        super().__init__(name, 100)
        super().showInfo()


class HeroStrength(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name, 200) # class Hero jika dirubah ini tidak otomatis berubah
        super().__init__(name, 200)
        super().showInfo()


lina = HeroIntelligent("lina")
axe = HeroStrength("axe")
