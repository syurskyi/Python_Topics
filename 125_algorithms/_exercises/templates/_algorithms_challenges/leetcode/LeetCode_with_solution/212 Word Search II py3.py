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
____ t___ _______ L..
____ c.. _______ d..


dirs [(0, 1), (0, -1), (-1, 0), (1, 0)]


c_ TrieNode:
    ___ -
        word N..
        children d..(TrieNode)


c_ Solution:
    ___ findWords  board: L..[L..[s..]], words: L..s.. __ L..[s..]:
        root construct(words)
        m, n l..(board), l..(board 0
        visited [[F.. ___ _ __ r..(n)] ___ _ __ r..(m)]
        ret s..()
        ___ i __ r..(m
            ___ j __ r..(n
                dfs(board, visited, i, j, root, ret)

        r.. l..(ret)

    ___ dfs  board, visited, i, j, cur, ret
        m, n l..(board), l..(board 0
        visited[i][j] T..
        c board[i][j]
        __ c __ cur.children:
            nxt cur.children[c]
            __ nxt.word __ n.. N..
                ret.add(nxt.word)

            ___ di, dj __ dirs:
                I i + di
                J j + dj
                __ 0 <_ I < m a.. 0 <_ J < n a.. n.. visited[I][J]:
                    dfs(board, visited, I, J, nxt, ret)

        visited[i][j] F..

    ___ construct  words
        root TrieNode()
        ___ w __ words:
            cur root
            ___ c __ w:
                cur cur.children[c]
            cur.word w

        r.. root
