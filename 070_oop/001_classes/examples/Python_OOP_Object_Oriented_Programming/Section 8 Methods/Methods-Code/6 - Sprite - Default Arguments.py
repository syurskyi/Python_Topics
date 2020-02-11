class Sprite:

    def __init__(self, character, x, y):
        self.character = character
        self._x = x
        self._y = y

    def move_forward(self, angle, step=5, movement="vertical"):
        if movement == "vertical":
            self._y += step
        else:
            self._x += step

    @property
    def y(self):
        return self._y

    @property
    def x(self):
        return self._x
