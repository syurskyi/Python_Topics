'''
Created on Feb 19, 2017

@author: MT
'''
c_ TrieNode(o..
    ___ - , c_ N..
        c = c
        children    # dict
        isLeaf = F..

___ buildTrie(words
    root = TrieNode()
    ___ word __ words:
        p = root
        ___ i, c __ e..(word
            __ c n.. __ p.children:
                t = TrieNode(c)
                p.children[c] = t
            ____:
                t = p.children[c]
            p = t
            __ i __ l..(word)-1:
                t.isLeaf = T..
    r.. root

c_ Solution(o..
    ___ findWords  board, words
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        result = s..()
        root = buildTrie(words)
        m, n = l..(board), l..(board[0])
        ___ i __ r..(m
            ___ j __ r..(n
                dfs(board, i, j, root, [], result)
        r.. l..(result)
    
    ___ dfs  board, i, j, p, elem, result
        c = board[i][j]
        __ c __ '#' o. c n.. __ p.children: r..
        p = p.children[c]
        __ p.isLeaf:
            elem.a..(c)
            result.add(''.j..(elem
            elem.pop()
        m, n = l..(board), l..(board[0])
        
        ___ x, y __ ((i, j+1), (i, j-1), (i+1, j), (i-1, j:
            __ 0 <= x < m a.. 0 <= y < n:
                board[i][j] = '#'
                elem.a..(c)
                dfs(board, x, y, p, elem, result)
                board[i][j] = c
                elem.pop()
        
    ___ test
        testCases = [
#             (
#                 [
#                     ['o','a','a','n'],
#                     ['e','t','a','e'],
#                     ['i','h','k','r'],
#                     ['i','f','l','v'],
#                 ],
#                 ['oath', 'pea', 'eat', 'rain'],
#             ),
#             (
#                 [['a']],
#                 ['a'],
#             ),
#             (
#                 [['a', 'a']],
#                 ['a']
#             ),
            (
                [
                     'a', 'b' ,
                     'c', 'd' ,
                ],
                ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"],
#                 ['ab'],
            ),
        ]
        ___ board, words __ testCases:
            result = findWords(board, words)
            print(result)
            print('-='*20 + '-')

__ _____ __ _____
    Solution().test()
