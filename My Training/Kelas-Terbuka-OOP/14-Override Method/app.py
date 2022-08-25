# Override Method
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("showInfo di class Hero")
        print("{} health: {}".format(
            self.name,
            self.health
        )
        )


class HeroIntelligent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)

    # override
    def showInfo(self):  # override method menimpa fungsi yang ada di superclass
        # super().showInfo("intelligent")
        print("showInfo di subclass HeroIntelligent")
        print("{} \n\tTipe: intelligent, \n\thealth: {}".format(
            self.name,
            self.health
        )
        )


class HeroStrength(Hero):
    def __init__(self, name):
        super().__init__(name, 200)


lina = HeroIntelligent("lina")
pudge = HeroStrength("pudge")

lina.showInfo()
pudge.showInfo()
