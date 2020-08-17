'''
Created on Feb 19, 2017

@author: MT
'''
class TrieNode(object
    ___ __init__(self, c=None
        self.c = c
        self.children = {}
        self.isLeaf = False

___ buildTrie(words
    root = TrieNode()
    ___ word in words:
        p = root
        ___ i, c in enumerate(word
            __ c not in p.children:
                t = TrieNode(c)
                p.children[c] = t
            ____
                t = p.children[c]
            p = t
            __ i __ le.(word)-1:
                t.isLeaf = True
    r_ root

class Solution(object
    ___ findWords(self, board, words
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        result = set()
        root = buildTrie(words)
        m, n = le.(board), le.(board[0])
        ___ i in range(m
            ___ j in range(n
                self.dfs(board, i, j, root, [], result)
        r_ list(result)
    
    ___ dfs(self, board, i, j, p, elem, result
        c = board[i][j]
        __ c __ '#' or c not in p.children: r_
        p = p.children[c]
        __ p.isLeaf:
            elem.append(c)
            result.add(''.join(elem))
            elem.p..
        m, n = le.(board), le.(board[0])
        
        ___ x, y in ((i, j+1), (i, j-1), (i+1, j), (i-1, j)):
            __ 0 <= x < m and 0 <= y < n:
                board[i][j] = '#'
                elem.append(c)
                self.dfs(board, x, y, p, elem, result)
                board[i][j] = c
                elem.p..
        
    ___ test(self
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
                    ['a', 'b'],
                    ['c', 'd'],
                ],
                ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"],
#                 ['ab'],
            ),
        ]
        ___ board, words in testCases:
            result = self.findWords(board, words)
            print(result)
            print('-='*20 + '-')

__ __name__ __ '__main__':
    Solution().test()
