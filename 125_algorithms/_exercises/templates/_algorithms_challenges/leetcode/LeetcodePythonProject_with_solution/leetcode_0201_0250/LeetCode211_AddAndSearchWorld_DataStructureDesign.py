'''
Created on Feb 19, 2017

@author: MT
'''

class TrieNode(object):
    ___ __init__(self, c_ N..
        self.c = c
        self.children = {}
        self.isLeaf = False

class WordDictionary(object):
    ___ __init__(self):
        self.root = TrieNode()
    
    ___ addWord(self, word):
        children = self.root.children
        ___ i, c __ e..(word):
            __ c __ children:
                t = children[c]
            ____:
                t = TrieNode(c)
                children[c] = t
            children = t.children
            __ i __ l..(word)-1:
                t.isLeaf = True
    
    ___ searchDFS(self, children, word, startInd):
        __ startInd __ l..(word):
            r.. bool(n.. children)
        c = word[startInd]
        __ c __ children:
            __ startInd __ l..(word)-1 a.. children[c].isLeaf:
                r.. True
            r.. self.searchDFS(children[c].children, word, startInd+1)
        ____ c __ '.':
            ___ key, node __ children.iteritems():
                __ startInd __ l..(word)-1 a.. node.isLeaf:
                    r.. True
                __ self.searchDFS(children[key].children, word, startInd+1):
                    r.. True
            r.. False
        ____:
            r.. False
    
    ___ search(self, word):
        r.. self.searchDFS(self.root.children, word, 0)
    