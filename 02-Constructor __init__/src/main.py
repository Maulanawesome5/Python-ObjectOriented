#Template class
class Hero:
    def __init__(self, inputName, inputPower, inputArmor, inputHealth):
        self.name = inputName
        self.power = inputPower
        self.armor = inputArmor
        self.health = inputHealth

hero1 = Hero("sniper", 100, 10, 5)
hero2 = Hero("mirana", 100, 15, 1)
hero3 = Hero("sven", 150, 100, 0)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
