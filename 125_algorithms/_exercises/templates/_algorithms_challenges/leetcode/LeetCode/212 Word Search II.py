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
__author__ = 'Daniel'


class TrieNode(object
    ___ __init__(self, char
        self.char = char
        self.word = None
        self.children = {}  # map from char to TrieNode

    ___ __repr__(self
        r_ repr(self.char)


class Trie(object
    ___ __init__(self
        self.root = TrieNode(None)

    ___ add(self, word
        word = word.lower()
        cur = self.root
        for c in word:
            __ c not in cur.children:
                cur.children[c] = TrieNode(c)
            cur = cur.children[c]
        cur.word = word


class Solution:
    ___ __init__(self
        self.dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    ___ findWords(self, board, words
        """
        Trie+dfs
        pure Trie solution

        :param board: a list of lists of 1 length string
        :param words: a list of string
        :return: a list of string
        """
        trie = Trie()
        for word in words:
            trie.add(word)

        ret = set()
        marked = set()
        for i in xrange(le.(board)):
            for j in xrange(le.(board[0])):
                self.dfs(board, i, j, trie.root, marked, ret)

        r_ list(ret)

    ___ dfs(self, board, i, j, parent, marked, ret
        """
        :type parent: TrieNode
        """
        m = le.(board)
        n = le.(board[0])
        marked.add((i, j))
        c = board[i][j]

        __ c in parent.children:
            cur = parent.children[c]
            __ cur.word:
                ret.add(cur.word)
            for dir in self.dirs:
                row = i+dir[0]
                col = j+dir[1]
                __ 0 <= row < m and 0 <= col < n and (row, col) not in marked:
                    self.dfs(board, row, col, cur, marked, ret)

        marked.remove((i, j))