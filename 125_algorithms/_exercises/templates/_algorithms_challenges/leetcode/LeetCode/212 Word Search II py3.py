#!/usr/bin/python3
"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""
from typing ______ List
from collections ______ defaultdict


dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]


class TrieNode:
    ___ __init__(self
        self.word = None
        self.children = defaultdict(TrieNode)


class Solution:
    ___ findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.construct(words)
        m, n = le.(board), le.(board[0])
        visited = [[False ___ _ in range(n)] ___ _ in range(m)]
        ret = set()
        ___ i in range(m
            ___ j in range(n
                self.dfs(board, visited, i, j, root, ret)

        r_ list(ret)

    ___ dfs(self, board, visited, i, j, cur, ret
        m, n = le.(board), le.(board[0])
        visited[i][j] = True
        c = board[i][j]
        __ c in cur.children:
            nxt = cur.children[c]
            __ nxt.word is not None:
                ret.add(nxt.word)

            ___ di, dj in dirs:
                I = i + di
                J = j + dj
                __ 0 <= I < m and 0 <= J < n and not visited[I][J]:
                    self.dfs(board, visited, I, J, nxt, ret)

        visited[i][j] = False

    ___ construct(self, words
        root = TrieNode()
        ___ w in words:
            cur = root
            ___ c in w:
                cur = cur.children[c]
            cur.word = w

        r_ root
