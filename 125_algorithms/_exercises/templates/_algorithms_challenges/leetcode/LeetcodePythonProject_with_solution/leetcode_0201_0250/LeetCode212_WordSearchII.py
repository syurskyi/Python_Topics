'''
Created on Feb 19, 2017

@author: MT
'''
class TrieNode(object):
    ___ __init__(self, c_ N..
        self.c = c
        self.children = {}
        self.isLeaf = False

___ buildTrie(words):
    root = TrieNode()
    for word in words:
        p = root
        for i, c in enumerate(word):
            __ c not in p.children:
                t = TrieNode(c)
                p.children[c] = t
            else:
                t = p.children[c]
            p = t
            __ i == len(word)-1:
                t.isLeaf = True
    return root

class Solution(object):
    ___ findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        result = set()
        root = buildTrie(words)
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                self.dfs(board, i, j, root, [], result)
        return list(result)
    
    ___ dfs(self, board, i, j, p, elem, result):
        c = board[i][j]
        __ c == '#' or c not in p.children: return
        p = p.children[c]
        __ p.isLeaf:
            elem.append(c)
            result.add(''.join(elem))
            elem.pop()
        m, n = len(board), len(board[0])
        
        for x, y in ((i, j+1), (i, j-1), (i+1, j), (i-1, j)):
            __ 0 <= x < m and 0 <= y < n:
                board[i][j] = '#'
                elem.append(c)
                self.dfs(board, x, y, p, elem, result)
                board[i][j] = c
                elem.pop()
        
    ___ test(self):
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
        for board, words in testCases:
            result = self.findWords(board, words)
            print(result)
            print('-='*20 + '-')

__ __name__ == '__main__':
    Solution().test()
