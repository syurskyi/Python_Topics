class Warrior:
    ___ __init__(self,name
        self.name = name
        self.health = 100
        self.visible = True
        
    ___ strike(self,enemy,swings
        #health cannot go below zero
        enemy.health = max([0,enemy.health-(swings*10)]) __ enemy.visible else enemy.health

    ___ hide(self
        self.visible = not(self.visible)

ninja = Warrior('Ninja')
samurai = Warrior('Samurai')
ninja.hide()
samurai.strike(ninja, 3)
print(ninja.health)
# ninja.health should == 70