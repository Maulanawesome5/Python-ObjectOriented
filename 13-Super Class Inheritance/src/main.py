class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def HeroInfo(self):
        print(f"(HP: {self.health}) {self.name}")


class Hero_Intelligent(Hero):
    def __init__(self, name):
        # Cara inherit constructor pertama
        Hero.__init__(self, name, 100)

        # Cara inherit method pertama
        Hero.HeroInfo(self)


class Hero_Strength(Hero):
    def __init__(self, name):
        # Cara inherit constructor kedua
        super().__init__(name, 200)

        # Cara inherit method kedua
        super().HeroInfo()


lina = Hero_Intelligent("Lina")
techies = Hero_Intelligent("Techies")
axe = Hero_Strength("Axe")
swordMaster = Hero_Strength("Sword Master")


