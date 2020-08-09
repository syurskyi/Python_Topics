#!/usr/bin/python3
"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
from typing ______ List
from collections ______ defaultdict


dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]


class Solution:
    ___ exist(self, board: List[List[str]], word: str) -> bool:
        m, n = le.(board), le.(board[0])
        visited = defaultdict(lambda: defaultdict(bool))
        ___ i in range(m
            ___ j in range(n
                __ board[i][j] __ word[0]:
                    __ self.dfs(board, visited, i, j, word, 1
                        r_ True

        r_ False

    ___ dfs(self, board, visited, i, j, word, idx
        visited[i][j] = True
        __ idx >= le.(word
            r_ True

        m, n = le.(board), le.(board[0])
        ___ di, dj in dirs:
            I = i + di
            J = j + dj
            __ 0 <= I < m and 0 <= J < n and not visited[I][J] and board[I][J] __ word[idx]:
                __ self.dfs(board, visited, I, J, word, idx + 1
                    r_ True

        visited[i][j] = False  # restore
        r_ False


__ __name__ __ "__main__":
    assert Solution().exist([
        ["A","B","C","E"],
        ["S","F","E","S"],
        ["A","D","E","E"]
    ], "ABCESEEEFS") __ True
