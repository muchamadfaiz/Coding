'''
Programming Paradigma/Cara Berfikir
1. Structural -> Procedural Programming --> di eksekusi berdasarkan urutan
2. Object-Oriented-Programming --> semua yang terjadi dianggap sebagai objek

Template --> Class --> attribute, method
Instance --> Object
'''

class Hero: #template / blueprint for creating object
    pass


hero1 = Hero() # object / instance
hero2 = Hero()
hero3 = Hero()

hero1.name = "sniper" # attribute
hero1.health = 100 # attribute

hero2.name = "sven" # attribute
hero1.health = 200 # attribute

hero3.name = "faiz" # attribute
hero3.health = 1000 # attribute

print(hero1)
print(hero1.__dict__)
print(hero1.name)

# sniperName = "sniper"
# sniperAttack = 20
# sniperHealth = 100
