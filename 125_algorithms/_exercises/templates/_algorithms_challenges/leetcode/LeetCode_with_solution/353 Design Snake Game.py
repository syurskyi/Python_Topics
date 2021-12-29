"""
Design a Snake game that is played on a device with screen size = width x height.
"""
____ collections _______ deque

__author__ = 'Daniel'


class SnakeGame(object):
    ___ __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.w = width
        self.h = height
        self.food = deque(food)
        self.body = deque([(0, 0)])
        self.dirs = {
            'U': (-1, 0),
            'L': (0, -1),
            'R': (0, 1),
            'D': (1, 0),
        }
        self.eat = 0

    ___ move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        x, y = self.body[0]
        dx, dy = self.dirs[direction]
        x += dx
        y += dy
        fx, fy = self.food[0] __ self.food ____ (-1, -1)
        __ x __ fx a.. y __ fy:
            self.food.popleft()
            self.eat += 1
        ____:
            self.body.pop()
            __ (x, y) __ self.body o. n.. (0 <= x < self.h a.. 0 <= y < self.w):
                # possible to use set to accelerate check
                r.. -1

        self.body.appendleft((x, y))
        r.. self.eat


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

__ __name__ __ "__main__":
    game = SnakeGame(3, 2, [[1, 2], [0, 1]])
    ___ char, expect __ z..('RDRULU', [0, 0, 1, 1, 2, -1]):
        ... game.move(char) __ expect
