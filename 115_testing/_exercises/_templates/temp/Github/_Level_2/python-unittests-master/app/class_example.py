"""
Solver of fifteen puzzle
https://en.wikipedia.org/wiki/15_puzzle
"""

import array


c_ Board:
    """
    Instance of this class represents one state of the board in the Fifteen puzzle
    """
    _solved_board = [
            array.array('B', [1, 2, 3, 4]),
            array.array('B', [5, 6, 7, 8]),
            array.array('B', [9, 10, 11, 12]),
            array.array('B', [13, 14, 15, 0])
    ]

    ___  -   rows, check=True):
        self._rows = rows

        if check:
            self.check()

    ___ check(self):
        for i in range(16):
            # check number i is at least in one row
            if not any(map(lambda row: i in row, self._rows)):
                raise ValueError("Number {i} is missing in the input data".format(**locals()))

    ___ is_solved(self):
        return self._rows == self._solved_board


c_ FifteenSolver:
    ___  -   board):
        self.board = board

    ___ solve(self):
        # TODO implement using BFS from https://github.com/TheAlgorithms/Python/blob/master/Graphs/basic-graphs.py
        pass
