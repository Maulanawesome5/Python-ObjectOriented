class Hero:
    def __init__(self, name, health, attackPower, armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber
    
    def serang(self, musuh):
        print(self.name + ' menyerang ' + musuh.name)
        musuh.diserang(self, self.attackPower)

    def diserang(self, musuh, attackPower_musuh):
        print(self.name + ' diserang ' + musuh.name)
        attack_diterima = attackPower_musuh / self.armorNumber
        print('Serangan terasa : ' + str(attack_diterima))
        self.health -= attack_diterima
        print('Health ' + self.name + ' tersisa ' + str(self.health))


sniper = Hero('sniper', 100, 10, 5)
barbar = Hero('barbar', 100, 20, 10)

sniper.serang(barbar)
print("\n")
barbar.serang(sniper)
