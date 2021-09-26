#Template class 
# keyword pass digunakan jika tidak memberikan argumen apapun pada class
class Hero:
    pass

hero1 = Hero() #Object / instance
hero2 = Hero() #Object / instance
hero3 = Hero() #Object / instance

hero1.name = "sniper"
hero1.health = 100
hero2.name = "sven"
hero2.health = 200
hero3.name = "axe"
hero3.health = 150

print(hero1)
print(hero1.__dict__)
print(hero1.name)