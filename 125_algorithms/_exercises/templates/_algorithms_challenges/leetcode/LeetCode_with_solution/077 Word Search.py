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
c_ Solution:
    ___ exist(self, board, word):
        """
        dfs
        :param board: a list of lists of 1 length string
        :param word: a string
        :return: boolean
        """
        __ n.. board:
            r..
        # unpack
        # board = [item[0] for item in board]

        m = l..(board)
        n = l..(board[0])
        visited = [[F.. ___ _ __ xrange(n)] ___ _ __ xrange(m)]  # avoid loop
        ___ i __ xrange(m):
            ___ j __ xrange(n):
                __ board[i][j]__word[0]:
                    visited[i][j] = T..
                    __ s..(board, i, j, word[1:], visited):
                        r.. T..
                    visited[i][j] = F..
        r.. F..

    ___ s..(self, board, pre_row, pre_col, word, visited):
        __ n.. word:
            r.. T..
        # searching for word[0]
        m = l..(board)
        n = l..(board[0])
        next_positions = [(pre_row-1, pre_col), (pre_row+1, pre_col), (pre_row, pre_col-1), (pre_row, pre_col+1)]  # four directions
        ___ next_position __ next_positions:
            __ 0<=next_position[0]<m a.. 0<=next_position[1]<n:  # pre-checking
                __ visited[next_position[0]][next_position[1]]__False a.. board[next_position[0]][next_position[1]]__word[0]:
                    visited[next_position[0]][next_position[1]] = T..
                    __ s..(board, next_position[0], next_position[1], word[1:], visited):
                        r.. T..
                    visited[next_position[0]][next_position[1]] = F..  # restore
        r.. F..



__ __name____"__main__":
    board = [
        "ABCE",
        "SFCS",
        "ADEE"
    ]
    word = "ABCCED"
    print Solution().exist(board, word)