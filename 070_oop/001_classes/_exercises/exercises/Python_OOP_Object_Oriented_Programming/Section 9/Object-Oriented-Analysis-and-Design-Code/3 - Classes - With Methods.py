import random

class Player:
    max_x = 450
    max_y = 450

    # Added to move the Player
    speed = 20

    def __init__(self, x, y, character):
        self._x = x
        self._y = y
        self._num_lives = 10 # Initial value
        self._character = character

    def move_up(self):
        self._y += Player.speed

    def move_down(self):
        self._y -= Player.speed

    def move_left(self):
        self._x -= Player.speed

    def move_right(self):
        self._x += Player.speed

    def display_welcome(self, message="Welcome to the game"):
        print(message)

    def shoot_candy(self):
        return Candy(self._x, self._y)

    def lose_life(self):
        self._num_lives -= 1

class Candy:
    speed = 40

    def __init__(self, x, y, type_of_movement="horizontal"):
        self._x = x
        self._y = y
        self._type_of_movement = type_of_movement

    def move(self):
        if self._type_of_movement == "horizontal":
            self._x += Candy.speed
        else:
            self._y += Candy.speed

    def is_beyond_boundaries(self):
        return  (self._x > 450 or self._x < 0) or (self._y > 450 or self._y < 0)  

class Enemy:
    max_x = 450
    max_y = 450

    def __init__(self, x, y, speed, type_of_movement="vertical",):
        self._x = random.randint(0, max_x)
        self._y = random.randint(0, max_y)
        self._type_of_movement = type_of_movement
        self._num_lives = 15 # Initial value
        self._speed = speed

    def move(self):
        if self._type_of_movement == "vertical":
            self._y += self._speed
        else:
            self._x += self._speed

    def change_type_of_movement(self):
        if self._type_of_movement == "vertical":
            self._type_of_movement = "horizontal"
        else:
            self._type_of_movement = "vertical"

    def lose_life(self):
        if self._num_lives > 0:
            self._num_lives -= 1



        

    


