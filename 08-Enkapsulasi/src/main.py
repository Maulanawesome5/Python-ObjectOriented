"""
Encapsulation / enkapsulasi adalah membuat semua variabel
menjadi private. Untuk mengakses data yang dibutuhkan, menggunakan
getter dan setter
"""
class Hero:

    def __init__(self, name, health, attackPower):
        self.__name = name
        self.__health = health
        self.__attPower = attackPower

    #===================== getter =====================
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health

    #===================== setter =====================
    def diserang(self, serangPower):
        self.__health -= serangPower

    def setAttackPower(self, nilaibaru):
        self.__attPower = nilaibaru

# Awal dari game
archer = Hero("Archer", 100, 70)

# Game berjalan
print("Kelas dari pahlawan ", archer.getName())
print("Health Point tersedia ", archer.getHealth())
archer.diserang(5)
print("Health Point tersisa ", archer.getHealth())

