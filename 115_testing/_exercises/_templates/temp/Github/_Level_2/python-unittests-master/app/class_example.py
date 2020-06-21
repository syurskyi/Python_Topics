"""
Solver of fifteen puzzle
https://en.wikipedia.org/wiki/15_puzzle
"""

______ array


c_ Board:
    """
    Instance of this class represents one state of the board in the Fifteen puzzle
    """
    _solved_board _ [
            array.array('B', [1, 2, 3, 4]),
            array.array('B', [5, 6, 7, 8]),
            array.array('B', [9, 10, 11, 12]),
            array.array('B', [13, 14, 15, 0])
    ]

    ___  -   rows, check_True
        _rows _ rows

        __ check:
            check()

    ___ check
        ___ i __ ra..(16
            # check number i is at least in one row
            __ no. any(map(l___ row: i __ row, _rows)):
                r_ V..("Number {i} is missing in the input data".f..(**locals()))

    ___ is_solved
        r_ _rows __ _solved_board


c_ FifteenSolver:
    ___  -   board
        board _ board

    ___ solve
        # TODO implement using BFS from https://github.com/TheAlgorithms/Python/blob/master/Graphs/basic-graphs.py
        p..
