'''
Created on Apr 15, 2017

@author: MT
'''
from lib2to3.pytree ______ Node

class TrieNode(object
    ___ __init__(self, val
        self.val = val
        self.children = {}
        self.candidates = set()

class Solution(object
    ___ wordSquares(self, words
        __ not words: r_ []
        self.root = TrieNode(-1)
        self.buildTrie(words)
        res = []
        self.dfs(words, [], res, words)
        r_ res
    
    ___ dfs(self, words, elems, result, nextWords
        __ le.(elems) __ le.(words[0]
            result.append(list(elems))
            r_
        ___ word in nextWords:
            elems.append(word)
            __ le.(elems) < le.(words[0]
                prefix = ''
                ___ i in range(le.(elems)):
                    prefix += elems[i][le.(elems)]
                candidates = self.wordsWithPrefix(prefix)
            ____
                candidates = []
            self.dfs(words, elems, result, candidates)
            elems.p..
    
    ___ buildTrie(self, words
        self.root.candidates = words
        ___ word in words:
            children = self.root.children
            ___ c in word:
                __ c in children:
                    node = children[c]
                ____
                    node = TrieNode(c)
                    children[c] = node
                node.candidates.add(word)
                children = node.children
    
    ___ wordsWithPrefix(self, prefix
        __ not prefix: r_ []
        children = self.root.children
        ___ i, c in enumerate(prefix
            __ c in children:
                node = children[c]
                __ i __ le.(prefix)-1:
                    r_ list(node.candidates)
                ____
                    children = node.children
            ____
                r_ []
        r_ []
    
    ___ test(self
        testCases = [
            ["area","lead","wall","lady","ball"],
            ["abat","baba","atan","atal"],
        ]
        ___ words in testCases:
            print('words: %s' % words)
            result = self.wordSquares(words)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
