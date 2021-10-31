class Hero:
    #Class variable
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        #Instance variabel / variabel yang dimiliki oleh class Hero
        self.name = inputName
        self.power = inputPower
        self.armor = inputArmor
        self.health = inputHealth
        Hero.jumlah += 1
        print("Menambah object Hero baru bernama " + inputName)

hero1 = Hero("sniper", 100, 10, 5)
print(Hero.jumlah)
hero2 = Hero("mirana", 100, 15, 1)
print(Hero.jumlah)
hero3 = Hero("sven", 150, 100, 0)
print(Hero.jumlah)
