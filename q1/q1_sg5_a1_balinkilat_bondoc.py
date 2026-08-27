class hero:
    def __init__(self, name, hp = 100):
        self.name = name
        self.hp = hp

    def take_damage(self, damage):
        self.hp -= damage
        
myHero = hero("Arthur")
myHero2 = hero("Morgana")
myHero.take_damage(10)
print("Arthur's hp goes from 100 to", myHero.hp,".")
print("Morgana's hp goes from 100 to", myHero2.hp,".")
