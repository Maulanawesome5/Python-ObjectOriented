class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health


class Hero_Intelligent(Hero):
    pass


class Hero_Strength(Hero):
    pass


lina = Hero("Lina", 100)
techies = Hero_Intelligent("Techies", 100)
axe = Hero_Strength("Axe", 200)

print(lina.__dict__)
print(techies.__dict__)
print(axe.__dict__)
print(help(techies))
print(help(axe))
