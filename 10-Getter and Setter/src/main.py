class Hero:
    
    def __init__(self, name, health, armor):
        self.__name = name
        self.__health = health
        self.__armor = armor
        # self.info = f"Hero Name : {self.__name}\
        # \nHP: {self.__health} \tAP: {self.__armor}"
    
    @property
    def info(self):
        # Decorator property, mengubah method agar bisa
        # menjadi seperti variabel
        return f"Hero Name : {self.__name}\
        \nHP: {self.__health} \tAP: {self.__armor}"
    
    @property
    def armor(self):
        pass
    
    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, inputNum):
        self.__armor = inputNum

    @armor.deleter
    def armor(self):
        print("Nilai class variabel armor dihapus.")
        self.__armor = None


# Instance
print(5*"=" + " Membuat property method 'info' ")
sniper = Hero("Sniper", 100, 10)
print(sniper.info)

print("\n" + 5*"=" + " Membuat getter dan setter ")
print("Getter -> Nilai armor = ", sniper.armor)
sniper.armor = 35
print("Setter -> Nilai armor = ", sniper.armor)
print(sniper.info)

print("\n" + 5*"=" + " Membuat deleter")
del sniper.armor
print(sniper.info)