'''
Created on Feb 18, 2017

@author: MT
'''

c_ TrieNode(object):
    ___ - , s = N..):
        c = s
        children    # dict
        isLeaf = F..

c_ Trie(object):
    ___ - ):
        root = TrieNode()
    
    ___ insert(self, word):
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
    
    ___ searchNode(self, word):
        children = root.children
        ___ c __ word:
            __ c __ children:
                t = children[c]
                children = t.children
            ____:
                r.. N..
        r.. t
    
    ___ s..(self, word):
        t = searchNode(word)
        r.. bool(t a.. t.isLeaf)
    
    ___ startsWith(self, prefix):
        t = searchNode(prefix)
        r.. bool(t __ n.. N..)
    
    