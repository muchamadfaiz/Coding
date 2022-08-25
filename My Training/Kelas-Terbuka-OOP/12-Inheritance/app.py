# Inheritance (pewarisan)
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health


class HeroStrength(Hero):
    pass


class HeroIntelligent(Hero):
    pass


pudge = HeroStrength("pudge", 1000)
techies = HeroIntelligent("techies", 5)
print(help(techies))
# print(techies.name)
