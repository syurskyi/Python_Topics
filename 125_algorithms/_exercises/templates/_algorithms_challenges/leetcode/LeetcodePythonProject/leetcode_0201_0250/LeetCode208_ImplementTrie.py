'''
Created on Feb 18, 2017

@author: MT
'''

class TrieNode(object
    ___ __init__(self, s = None
        self.c = s
        self.children = {}
        self.isLeaf = False

class Trie(object
    ___ __init__(self
        self.root = TrieNode()
    
    ___ insert(self, word
        children = self.root.children
        ___ i, c __ enumerate(word
            __ c __ children:
                t = children[c]
            ____
                t = TrieNode(c)
                children[c] = t
            children = t.children
            __ i __ le.(word)-1:
                t.isLeaf = True
    
    ___ searchNode(self, word
        children = self.root.children
        ___ c __ word:
            __ c __ children:
                t = children[c]
                children = t.children
            ____
                r_ None
        r_ t
    
    ___ search(self, word
        t = self.searchNode(word)
        r_ bool(t and t.isLeaf)
    
    ___ startsWith(self, prefix
        t = self.searchNode(prefix)
        r_ bool(t pa__ not None)
    
    