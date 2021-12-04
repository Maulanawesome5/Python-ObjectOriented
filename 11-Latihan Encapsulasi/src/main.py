class Hero:
    
    # private class variabel
    __jumlah = 0

    def __init__(self, name, health, attack, armor):
        self.__Name = name
        self.__HealthBasePoint = health
        self.__AttackPowerBase = attack
        self.__Armor = armor
        self.__Level = 1
        self.__Experience = 0

        self.__HealthMax = self.__HealthBasePoint * self.__Level
        self.__Damage = self.__AttackPowerBase * self.__Level
        self.__Protection = self.__Armor * self.__Level

        self.__Health = self.__HealthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return f"Hero Name -> {self.__Name}, Lv. {self.__Level} \
        \nHP: {self.__Health}/{self.__HealthMax} \tAP: {self.__Damage} \tProtection: {self.__Protection} \
        \nEXP {self.__Experience}"

    @property
    def gainExperience(self):
        pass

    @gainExperience.setter
    def gainExperience(self, addExp):
        self.__Experience += addExp
        if (self.__Experience >= 100):
            print(self.__Name, 'level up')
            self.__Level += 1
            self.__Experience -= 100
            self.__HealthMax = self.__HealthBasePoint * self.__Level
            self.__Damage = self.__AttackPowerBase * self.__Level
            self.__Protection = self.__Armor * self.__Level

    def attack(self, musuh):
        self.gainExperience = 50



# Instance
berserker = Hero("Berserker", 300, 25, 40)
saber = Hero("Saber", 150, 15, 50)
# print(berserker.info)
# print(saber.info)

berserker.attack(saber)
berserker.attack(saber)
saber.attack(berserker)
saber.attack(berserker)
saber.attack(berserker)

print(berserker.info)
print(saber.info)