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


c_ TrieNode(o..):
    ___ - , char):
        char = char
        word = N..
        children    # dict  # map from char to TrieNode

    ___  -r
        r.. repr(char)


c_ Trie(o..):
    ___ - ):
        root = TrieNode(N..)

    ___ add  word):
        word = word.l..
        cur = root
        ___ c __ word:
            __ c n.. __ cur.children:
                cur.children[c] = TrieNode(c)
            cur = cur.children[c]
        cur.word = word


c_ Solution:
    ___ - ):
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    ___ findWords  board, words):
        """
        Trie+dfs
        pure Trie solution

        :param board: a list of lists of 1 length string
        :param words: a list of string
        :return: a list of string
        """
        trie = Trie()
        ___ word __ words:
            trie.add(word)

        ret = s..()
        marked = s..()
        ___ i __ x..(l..(board)):
            ___ j __ x..(l..(board[0])):
                dfs(board, i, j, trie.root, marked, ret)

        r.. l..(ret)

    ___ dfs  board, i, j, parent, marked, ret):
        """
        :type parent: TrieNode
        """
        m = l..(board)
        n = l..(board[0])
        marked.add((i, j))
        c = board[i][j]

        __ c __ parent.children:
            cur = parent.children[c]
            __ cur.word:
                ret.add(cur.word)
            ___ dir __ dirs:
                row = i+dir[0]
                col = j+dir[1]
                __ 0 <= row < m a.. 0 <= col < n a.. (row, col) n.. __ marked:
                    dfs(board, row, col, cur, marked, ret)

        marked.remove((i, j))