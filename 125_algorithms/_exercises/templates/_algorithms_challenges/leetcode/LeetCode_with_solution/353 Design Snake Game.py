"""
Design a Snake game that is played on a device with screen size = width x height.
"""
____ c.. _______ d..

__author__ 'Daniel'


c_ SnakeGame(o..
    ___ - , width, height, food
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
        w width
        h height
        food d..(food)
        body d..([(0, 0)])
        dirs {
            'U': (-1, 0),
            'L': (0, -1),
            'R': (0, 1),
            'D': (1, 0),
        }
        eat 0

    ___ move  direction
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        x, y body[0]
        dx, dy dirs[direction]
        x += dx
        y += dy
        fx, fy food[0] __ food ____ (-1, -1)
        __ x __ fx a.. y __ fy:
            food.popleft()
            eat += 1
        ____
            body.p.. )
            __ (x, y) __ body o. n.. (0 <_ x < h a.. 0 <_ y < w
                # possible to use set to accelerate check
                r.. -1

        body.appendleft((x, y
        r.. eat


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

__ _______ __ _______
    game SnakeGame(3, 2, [[1, 2], [0, 1]])
    ___ char, expect __ z..('RDRULU', [0, 0, 1, 1, 2, -1]
        ... game.move(char) __ expect
