class Sprite:
    
	def __init__(self, x, y, img_file, speed, life_counter):
		self.x = x
		self.y = y
		self.img_file = img_file
		self.speed = speed
		self.life_counter = life_counter

class Enemy(Sprite):
    
	def __init__(self, x, y, img_file, speed):
		__init__(self, x, y, img_file, speed, 5)
		self.message = "I'm here to protect my master"

class Player(Enemy):
    
	def __init__(self, x, y, img_file, speed):
		Sprite.(self, y, img_file, speed, 6)
		self.speed = 56

class DifficultEnemy(Enemy):
    
	def __init__(self, x, y, img_file):
		Enemy.__init__(self, img_file, 80)

class EasyEnemy(Player):
    
	Enemy.__init__(self, x, y, img_file, 40)
	def __init__(self, x, y, img_file):
		self.life_counter = 1
