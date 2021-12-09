class Hero:
    def __init__(self, name):
        self.HealthPool = [0, 100, 200, 300, 400, 500]
        self.attPowerPool = [0, 10, 20, 30, 40, 50]
        self.armorPool = [0, 1, 2, 3, 4, 5]
        self.__Name = name
        self.__Exp = 0
        self.__Level = 0

    
    def HeroInfo(self):
        print(f"{self.__Name}, Lv. {self.__Level} \n\
        HP: {self.__Health}, DP: {self.__attPower}, AP: {self.__armor} \n\
        EXP {self.__Exp}")
    
    @property
    def HealthPool(self):
        pass
    
    @property
    def attPowerPool(self):
        pass
    
    @property
    def armorPool(self):
        pass
    
    @property
    def LevelUp(self):
        pass
    
    @property
    def GainExp(self):
        pass

    @HealthPool.setter
    def HealthPool(self, input):
        self.__HealthPool = input
    
    @attPowerPool.setter
    def attPowerPool(self, input):
        self.__attPowerPool = input
    
    @armorPool.setter
    def armorPool(self, input):
        self.__armorPool = input

    @GainExp.setter
    def GainExp(self, input):
        self.__Exp += input
        if(self.__Exp >= 100):
            self.__LevelUp = self.__Exp // 100
            self.__Exp %= 100
    
    @LevelUp.setter
    def LevelUp(self, input):
        self.__Level += input
        self.__Health = self.__HealthPool[self.__Level]
        self.__attPower = self.__attPowerPool[self.__Level]
        self.__armor = self.__armorPool[self.__Level]


class Hero_Intelligent(Hero):

    def __init__(self, name):
        super().__init__(name)
        self.HealthPool = [0, 50, 100, 150, 200, 250]
        self.attPowerPool = [0, 20, 40, 60, 80, 100]
        self.armorPool = [0, 0.5, 1, 1.5, 2, 2.5]
        self.LevelUp = 1
        
        super().HeroInfo()


class Hero_Strength(Hero):

    def __init__(self, name):
        super().__init__(name)
        self.HealthPool = [0, 200, 300, 400, 500, 600]
        self.attPowerPool = [0, 20, 40, 60, 80, 100]
        self.armorPool = [0, 2, 4, 6, 8, 10]
        self.LevelUp = 1

        super().HeroInfo()

