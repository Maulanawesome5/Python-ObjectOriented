class Hero:
    # Class variabel
    jumlah_hero = 0
    __privateJumlah = 0

    # Variable instance
    def __init__(self, name, health):
        self.name = name
        self.health = health

        # Private variable instance
        self.__private = "private"
        # Protected variable instance
        self.__protected = "protected"

lancer = Hero("Lancer", 100)

print(lancer.__dict__)
print(Hero.__dict__)