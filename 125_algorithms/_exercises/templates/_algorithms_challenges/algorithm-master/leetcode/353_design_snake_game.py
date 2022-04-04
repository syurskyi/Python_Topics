"""
0. self.height is for `m`, self.width is for `n`
1. note that, REMOVE FIRST,
   MUST remove the snake tail **BEFORE** check it hit its body
2. this game is over if
    - hit wall
    - hit it self
    - no food

3. dont pop food in every move, just track its index
4. the score is just the len(body) - 1, except the head

5. what its return if no food or food is all taken?
6. does allow the snake just back if its body only 2?


Initially the snake appears at position (0,0) and the food at (1,2).
Your SnakeGame object will be instantiated and called as such:
obj = SnakeGame(width, height, food)
param_1 = obj.move(direction)


>>> snake = SnakeGame(3, 2, [[1, 2], [0, 1]])
>>> [snake.move(d) for d in 'RDRULU']
[0, 0, 1, 1, 2, -1]
>>> all(snake.move(d) == -1 for d in 'LUDR')
True

>>> snake = SnakeGame(3, 3, [[2, 0], [0, 0]])
>>> [snake.move(d) for d in 'DDUU']
[0, 1, 1, 2]
>>> all(snake.move(d) == -1 for d in 'RUDL')
True
"""
_______ c..


c_ SnakeGame:
    ___ - , width, height, food
        """
        :type width: int, screen width
        :type height: int, screen height
        :type food: List[List[int]], A list of food positions

        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1],
        the second is at [1,0].
        """
        __ n.. width o. n.. height o. n.. food:
            # raise error
            r..

        width = width
        height = height
        food = food
        fi = 0

        is_over = F..
        SCORE_IN_OVER = -1

        pos = [(0, 0)]
        snake = c...d..(pos)
        body = s..(pos)

        dn = {
            'U': (-1,  0),
            'D': ( 1,  0),
            'L': ( 0, -1),
            'R': ( 0,  1),
        }

    ___ move  direction
        """Moves the snake.
        :type direction: str, 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        :rtype: int, The game's score after the move. Return -1 if game over.

        Game over when snake crosses the screen boundary or bites its body.
        """
        __ direction n.. __ dn:
            # treat this move as invalid action
            r.. l..(snake) - 1

        __ is_over:
            # this game is over
            r.. SCORE_IN_OVER

        """
        new head will hit wall?
        """
        x, y = snake[0]
        dx, dy = dn[direction]
        hx = x + dx
        hy = y + dy

        __ n.. (0 <_ hx < height a.. 0 <_ hy < width
            is_over = T..
            r.. SCORE_IN_OVER

        """
        eat food or not
        """
        fx, fy = food[fi]

        __ fx __ hx a.. fy __ hy:
            # eat that food
            fi += 1
        ____
            # move to empty cell and need to remove tail
            tail = snake.p.. )
            body.discard(tail)

        """
        new head will hit its self?
        this detection MUST AFTER removing tail
        """
        __ (hx, hy) __ body:
            is_over = T..
            r.. SCORE_IN_OVER

        """
        new head is valid, track it
        """
        snake.appendleft((hx, hy
        body.add((hx, hy

        """
        There is no food anymore
        """
        __ fi >_ l..(food
            is_over = T..

        r.. l..(snake) - 1
