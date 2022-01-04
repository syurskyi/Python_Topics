'''
Created on Feb 19, 2017

@author: MT
'''

c_ TrieNode(object):
    ___ - , c_ N..
        c = c
        children    # dict
        isLeaf = F..

c_ WordDictionary(object):
    ___ - ):
        root = TrieNode()
    
    ___ addWord(self, word):
        children = root.children
        ___ i, c __ e..(word):
            __ c __ children:
                t = children[c]
            ____:
                t = TrieNode(c)
                children[c] = t
            children = t.children
            __ i __ l..(word)-1:
                t.isLeaf = T..
    
    ___ searchDFS(self, children, word, startInd):
        __ startInd __ l..(word):
            r.. bool(n.. children)
        c = word[startInd]
        __ c __ children:
            __ startInd __ l..(word)-1 a.. children[c].isLeaf:
                r.. T..
            r.. searchDFS(children[c].children, word, startInd+1)
        ____ c __ '.':
            ___ key, node __ children.iteritems
                __ startInd __ l..(word)-1 a.. node.isLeaf:
                    r.. T..
                __ searchDFS(children[key].children, word, startInd+1):
                    r.. T..
            r.. F..
        ____:
            r.. F..
    
    ___ s..(self, word):
        r.. searchDFS(root.children, word, 0)
    