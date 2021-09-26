class Hero:
    # Class variable
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # Instance variabel / variabel yang dimiliki oleh class Hero
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1
    
    # Void function, atau method tanpa return  
    def siapa(self):
        print("Hallo, saya pahlawan kelas " + self.name)

    # Method dengan argumen (contoh menambah health dari hero)
    def healthUp(self, up):
        self.health += up
    
    # Method dengan return (contoh mengurangi health dari hero)
    def getHealth(self, up):
        self.health -= up
        return self.health

hero1 = Hero("sniper", 100, 10, 5)
hero1.siapa()
print(hero1.__dict__)
hero1.healthUp(10)
print("Health bertambah jadi ",hero1.health)
print("Health berkurang jadi", hero1.getHealth(5))

hero2 = Hero("mirana", 100, 15, 1)
hero2.siapa()
print(hero2.__dict__)
hero2.healthUp(15)
print("Health bertambah jadi ",hero2.health)
print("Health berkurang jadi", hero2.getHealth(7))
