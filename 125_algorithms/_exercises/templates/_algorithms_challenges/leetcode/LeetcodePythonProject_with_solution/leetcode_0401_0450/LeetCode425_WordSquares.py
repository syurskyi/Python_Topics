'''
Created on Apr 15, 2017

@author: MT
'''
from lib2to3.pytree import Node

class TrieNode(object):
    ___ __init__(self, val):
        self.val = val
        self.children = {}
        self.candidates = set()

class Solution(object):
    ___ wordSquares(self, words):
        __ not words: return []
        self.root = TrieNode(-1)
        self.buildTrie(words)
        res = []
        self.dfs(words, [], res, words)
        return res
    
    ___ dfs(self, words, elems, result, nextWords):
        __ len(elems) == len(words[0]):
            result.append(list(elems))
            return
        for word in nextWords:
            elems.append(word)
            __ len(elems) < len(words[0]):
                prefix = ''
                for i in range(len(elems)):
                    prefix += elems[i][len(elems)]
                candidates = self.wordsWithPrefix(prefix)
            else:
                candidates = []
            self.dfs(words, elems, result, candidates)
            elems.pop()
    
    ___ buildTrie(self, words):
        self.root.candidates = words
        for word in words:
            children = self.root.children
            for c in word:
                __ c in children:
                    node = children[c]
                else:
                    node = TrieNode(c)
                    children[c] = node
                node.candidates.add(word)
                children = node.children
    
    ___ wordsWithPrefix(self, prefix):
        __ not prefix: return []
        children = self.root.children
        for i, c in enumerate(prefix):
            __ c in children:
                node = children[c]
                __ i == len(prefix)-1:
                    return list(node.candidates)
                else:
                    children = node.children
            else:
                return []
        return []
    
    ___ test(self):
        testCases = [
            ["area","lead","wall","lady","ball"],
            ["abat","baba","atan","atal"],
        ]
        for words in testCases:
            print('words: %s' % words)
            result = self.wordSquares(words)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ == '__main__':
    Solution().test()
