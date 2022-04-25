c_ Warrior:
    ___ - ,name
        ? ?
        health 100
        visible T..
        
    ___ strike enemy,swings
        #health cannot go below zero
        enemy.health m..([0,enemy.health-(swings*10)]) __ enemy.visible ____ enemy.health

    ___ hide
        visible n..(visible)

ninja Warrior('Ninja')
samurai Warrior('Samurai')
ninja.hide()
samurai.strike(ninja, 3)
print(ninja.health)
# ninja.health should == 70