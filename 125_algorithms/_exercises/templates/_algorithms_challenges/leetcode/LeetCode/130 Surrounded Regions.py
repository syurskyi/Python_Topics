"""
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""
__author__ = 'Danyang'
CONNECTED = 'C'
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    ___ solve(self, board
        """
        Graph Theory
        Algorithm1: bfs, to tell whether it is on the boarder
        Algorithm2: bfs, to get the connectivity graph
        :param board: a 2D array
        :return: NIL, Capture all regions by modifying the input board in-place.
        """
        __ not board or not board[0]:
            r_
        q = []
        # scan the boarder
        m = le.(board)
        n = le.(board[0])
        ___ i in xrange(m
            __ board[i][0]__'O': q.append((i, 0))
            __ board[i][n-1]__'O': q.append((i, n-1))
        ___ j in xrange(1, n-1
            __ board[0][j]__'O': q.append((0, j))
            __ board[m-1][j]__'O': q.append((m-1, j))


        w___ q: # dynamically expanding, no deletion of elements
            cor = q.p..
            board[cor[0]][cor[1]]=CONNECTED  # cannot be both "O" and CONNECTED
            ___ direction in directions:
                row = cor[0]+direction[0]
                col = cor[1]+direction[1]
                __ 0<=row<m and 0<=col<n and board[row][col]__'O':
                    q.append((row, col))


        ___ i in xrange(m
            ___ j in xrange(n
                __ board[i][j]__'O':
                    board[i][j] = 'X'
                ____ board[i][j]__CONNECTED:
                    board[i][j] = 'O'


__ __name____"__main__":
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    expected_board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    Solution().solve(board)
    assert board__expected_board




