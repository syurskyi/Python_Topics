"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or
vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  "ABCE",
  "SFCS",
  "ADEE"
]
* note, misrepresentation in the original question
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""
__author__ = 'Danyang'
class Solution:
    ___ exist(self, board, word
        """
        dfs
        :param board: a list of lists of 1 length string
        :param word: a string
        :return: boolean
        """
        __ not board:
            r_
        # unpack
        # board = [item[0] for item in board]

        m = le.(board)
        n = le.(board[0])
        visited = [[False ___ _ in xrange(n)] ___ _ in xrange(m)]  # avoid loop
        ___ i in xrange(m
            ___ j in xrange(n
                __ board[i][j]__word[0]:
                    visited[i][j] = True
                    __ self.search(board, i, j, word[1:], visited
                        r_ True
                    visited[i][j] = False
        r_ False

    ___ search(self, board, pre_row, pre_col, word, visited
        __ not word:
            r_ True
        # searching for word[0]
        m = le.(board)
        n = le.(board[0])
        next_positions = [(pre_row-1, pre_col), (pre_row+1, pre_col), (pre_row, pre_col-1), (pre_row, pre_col+1)]  # four directions
        ___ next_position in next_positions:
            __ 0<=next_position[0]<m and 0<=next_position[1]<n:  # pre-checking
                __ visited[next_position[0]][next_position[1]]__False and board[next_position[0]][next_position[1]]__word[0]:
                    visited[next_position[0]][next_position[1]] = True
                    __ self.search(board, next_position[0], next_position[1], word[1:], visited
                        r_ True
                    visited[next_position[0]][next_position[1]] = False  # restore
        r_ False



__ __name____"__main__":
    board = [
        "ABCE",
        "SFCS",
        "ADEE"
    ]
    word = "ABCCED"
    print Solution().exist(board, word)