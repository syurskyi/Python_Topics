import random

class Player:
    max_x = 450
    max_y = 450

    def __init__(self, x, y, character):
        self._x = x
        self._y = y
        self._num_lives = 10 # Initial value
        self._character = character

class Candy:
    speed = 40

    def __init__(self, x, y, type_of_movement="horizontal"):
        self._x = x
        self._y = y
        self._type_of_movement = type_of_movement

class Enemy:
    max_x = 450
    max_y = 450

    def __init__(self, x, y, speed, type_of_movement="vertical",):
        self._x = random.randint(0, max_x)
        self._y = random.randint(0, max_y)
        self._type_of_movement = type_of_movement
        self._num_lives = 15 # Initial value
        self._speed = speed


        
        

    


