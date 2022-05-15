class Team:
    # method setter
    def setTeam(self, team):
        self.team = team
    
    # method getter
    def DisplayTeam(self):
        print(self.team)


class Class_Servant:
    # method setter
    def setServantClass(self, classes):
        self.classes = classes

    # method getter
    def DisplayClasses(self):
        print(f'Servant Class -> {self.classes} \nName : {self.name}, HP : {self.health}')


class Servant(Team, Class_Servant):
    # constructor
    def __init__(self, name, health):
        self.name = name
        self.health = health


# Servant instance
saber1 = Servant('Mordred', 100)
saber1.setTeam('Red')
saber1.setServantClass('Saber')

saber1.DisplayClasses()
saber1.DisplayTeam()