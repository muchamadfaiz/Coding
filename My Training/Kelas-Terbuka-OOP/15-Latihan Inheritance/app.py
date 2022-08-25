# Latihan Inheritance
from Hero import HeroIntelligence, HeroStrength

lina = HeroIntelligence("lina")
slardar = HeroStrength("sladar")

lina.show_info()
slardar.show_info()

lina.gainExp = 200
slardar.gainExp = 250

lina.show_info()
slardar.show_info()
