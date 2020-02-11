class Enemy:

    speed = 8

    def __init__(self, x, y, difficulty):
        self.x = x
        self.y = y
        self.difficulty = difficulty

print(Enemy.speed) # Value 8

Enemy.speed = 15

print(Enemy.speed) # Value 15
