class Hero:

    # Private class variable
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    #===================== getter =====================
    def getJumlah(self):
        # Method ini hanya berlaku untuk object
        return Hero.__jumlah
    
    def getJumlah1():
        # Method ini tidak berlaku untuk object, 
        # tapi berlaku untuk class
        return Hero.__jumlah

    # Method static (decorator), nempel ke object dan class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah


saber = Hero("Saber")
print("Hero baru telah dibuat. Jumlah : ", Hero.getJumlah2())
archer = Hero("Archer")
print("Hero baru telah dibuat. Jumlah : ", archer.getJumlah2())
caster = Hero("Caster")
rider = Hero("Rider")
lancer = Hero("Lancer")
print("Hero baru telah dibuat. Jumlah : ", Hero.getJumlah3())

