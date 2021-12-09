class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def HeroInfo(self):
        print(f"(HP: {self.health}) {self.name}")


class Hero_Intelligent(Hero):
    def __init__(self, name):
        
        # constructor
        super().__init__(name, 100)
        
    # void method, override
    def HeroInfo(self):
        print(f"Hero class -> Intelligent \n\
        (HP: {self.health}) {self.name}")


class Hero_Strength(Hero):
    def __init__(self, name):
        
        # constructor
        super().__init__(name, 200)
        
        # void method
        super().HeroInfo() # jika memakai super(), indentasi harus sejajar dengan constructor


lina = Hero_Intelligent("Lina")
swordMaster = Hero_Strength("Sword Master")

lina.HeroInfo()
