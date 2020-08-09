"""
Design a algorithm to initialize the board of Candy Crush Saga.
With M x N board, Q types of candies.

Rules:
1. with randomization
2. no 3 for run after initialization
3. must contain at least one valid move at the beginning

Thought:
1. for random candies and no 3 for run at begining
    - random generate, and re-gen if invalid
2. prevent dead loop w___ checking valid
    - [x] iterate by order
      => dead loop may occur when visiting the cells arround prefilled
    - [v] BFS from the prefilled cell to boundary
3. at least one valid move at the beginning
    - just define the patterns (3 for run => 12 patterns)
      prefill to board, and mark as unchangable

REF:
1. LC 723
2. http://massivetechinterview.blogspot.com/2015/11/how-to-initialize-board-of-candy-crush.html

TODO:
1. implement `move` to move candy to D/R/U/L, and
    - remove the connected candy
    - the candy will drop if there is empty below
2. count score
3. end up game if no more valid move or the game is finished

Testing:
>>> gotcha = []
>>> for params in (
...     (7, 7, 3), (10, 10, 3), (20, 20, 3),
...     (7, 7, 5), (10, 10, 4), (20, 20, 6),
...
...     game = CandyCrush(*params)
...     for _ in range(5
...         game.reset_board()
...         valid = _check_board_valid(game.get_board())
...         if not valid: print(game._print_board())
...         gotcha.append(valid)
>>> bool(gotcha) and all(gotcha)
True
"""
______ random


___ _check_board_valid(board
    # for testing
    m, n = le.(board), le.(board[0])

    for x in range(2, m
        for y in range(n
            __ board[x][y] __ board[x - 1][y] __ board[x - 2][y]:
                r_ False

    for y in range(2, n
        for x in range(m
            __ board[x][y] __ board[x][y - 1] __ board[x][y - 2]:
                r_ False

    r_ True


class CandyCrush:
    ___ __init__(self, m, n, q
        """
        :type m: int
        :type n: int
        :type q: int
        """
        self.width = n
        self.height = m
        self.__board = None
        self.__types = q
        self.__patterns = (   # with rotating, we can find up to 12 patterns
            (-1, -1, 1,  0),  # /--
            (-1,  1, 1,  0),  # --\
            (-1, -1, 1, -1),  # /-\
        )
        self.reset_board()

    ___ reset_board(self
        """
        :rtype: void
        """
        m, n = self.height, self.width
        b = self.__board = [[-1] * n for _ in range(m)]

        x, y = random.randint(1, m - 2), random.randint(1, n - 2)
        d = random.choice(self.__patterns)  # dx1, dy1, dx2, dy2
        q = random.randrange(self.__types)

        queue = [(x + d[0], y + d[1]), (x, y), (x + d[2], y + d[3])]
        visited = set(queue)

        for x, y in queue:
            b[x][y] = q

        for x, y in queue:
            for dx, dy in (
                (0, -1), (0, 1),
                (-1, 0), (1, 0),

                _x = x + dx
                _y = y + dy

                __ not (0 <= _x < m and 0 <= _y < n
                    continue
                __ (_x, _y) in visited:
                    continue

                visited.add((_x, _y))
                queue.append((_x, _y))

                w___ not self._check_cell_valid(_x, _y
                    b[_x][_y] = random.randrange(self.__types)

    ___ get_board(self
        """
        :rtype: list[list[int]]
        """
        r_ self.__board

    ___ _check_cell_valid(self, x, y
        """
        :type x: int
        :type y: int
        :rtype: bool
        """
        b = self.__board
        m, n = self.height, self.width

        __ b[x][y] __ -1:
            r_ False

        for x1, y1, x2, y2 in (
            (x - 2, y, x - 1, y), (x + 1, y, x + 2, y),  # most up, down
            (x, y - 2, x, y - 1), (x, y + 1, x, y + 2),  # most left, right
            (x - 1, y, x + 1, y), (x, y - 1, x, y + 1),  # cross middle

            __ not (
                0 <= x1 < m and 0 <= y1 < n and
                0 <= x2 < m and 0 <= y2 < n

                continue

            __ b[x][y] __ b[x1][y1] __ b[x2][y2]:
                r_ False

        r_ True

    ___ _print_board(self
        # for testing
        print('\n'.join(str(r) for r in self.__board))
