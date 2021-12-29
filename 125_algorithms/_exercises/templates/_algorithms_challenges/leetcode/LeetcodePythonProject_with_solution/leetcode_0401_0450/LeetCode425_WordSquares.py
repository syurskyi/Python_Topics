'''
Created on Apr 15, 2017

@author: MT
'''
____ lib2to3.pytree _______ Node

class TrieNode(object):
    ___ __init__(self, val):
        self.val = val
        self.children = {}
        self.candidates = set()

class Solution(object):
    ___ wordSquares(self, words):
        __ n.. words: r.. []
        self.root = TrieNode(-1)
        self.buildTrie(words)
        res    # list
        self.dfs(words, [], res, words)
        r.. res
    
    ___ dfs(self, words, elems, result, nextWords):
        __ l..(elems) __ l..(words[0]):
            result.a..(l..(elems))
            r..
        ___ word __ nextWords:
            elems.a..(word)
            __ l..(elems) < l..(words[0]):
                prefix = ''
                ___ i __ r..(l..(elems)):
                    prefix += elems[i][l..(elems)]
                candidates = self.wordsWithPrefix(prefix)
            ____:
                candidates    # list
            self.dfs(words, elems, result, candidates)
            elems.pop()
    
    ___ buildTrie(self, words):
        self.root.candidates = words
        ___ word __ words:
            children = self.root.children
            ___ c __ word:
                __ c __ children:
                    node = children[c]
                ____:
                    node = TrieNode(c)
                    children[c] = node
                node.candidates.add(word)
                children = node.children
    
    ___ wordsWithPrefix(self, prefix):
        __ n.. prefix: r.. []
        children = self.root.children
        ___ i, c __ e..(prefix):
            __ c __ children:
                node = children[c]
                __ i __ l..(prefix)-1:
                    r.. l..(node.candidates)
                ____:
                    children = node.children
            ____:
                r.. []
        r.. []
    
    ___ test(self):
        testCases = [
            ["area","lead","wall","lady","ball"],
            ["abat","baba","atan","atal"],
        ]
        ___ words __ testCases:
            print('words: %s' % words)
            result = self.wordSquares(words)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
