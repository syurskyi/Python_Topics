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
____ typing _______ List
____ c.. _______ defaultdict


dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]


c_ Solution:
    ___ exist  board: List[List[s..]], word: s..) __ bool:
        m, n = l..(board), l..(board[0])
        visited = defaultdict(l....: defaultdict(bool))
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ board[i][j] __ word[0]:
                    __ dfs(board, visited, i, j, word, 1):
                        r.. T..

        r.. F..

    ___ dfs  board, visited, i, j, word, idx):
        visited[i][j] = T..
        __ idx >= l..(word):
            r.. T..

        m, n = l..(board), l..(board[0])
        ___ di, dj __ dirs:
            I = i + di
            J = j + dj
            __ 0 <= I < m a.. 0 <= J < n a.. n.. visited[I][J] a.. board[I][J] __ word[idx]:
                __ dfs(board, visited, I, J, word, idx + 1):
                    r.. T..

        visited[i][j] = F..  # restore
        r.. F..


__ _______ __ _______
    ... Solution().exist([
        ["A","B","C","E"],
        ["S","F","E","S"],
        ["A","D","E","E"]
    ], "ABCESEEEFS") __ T..
