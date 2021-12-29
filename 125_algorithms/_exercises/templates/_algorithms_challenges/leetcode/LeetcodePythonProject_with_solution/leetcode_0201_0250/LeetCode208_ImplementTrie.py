'''
Created on Feb 18, 2017

@author: MT
'''

class TrieNode(object):
    ___ __init__(self, s = None):
        self.c = s
        self.children = {}
        self.isLeaf = False

class Trie(object):
    ___ __init__(self):
        self.root = TrieNode()
    
    ___ insert(self, word):
        children = self.root.children
        for i, c in enumerate(word):
            __ c in children:
                t = children[c]
            else:
                t = TrieNode(c)
                children[c] = t
            children = t.children
            __ i == len(word)-1:
                t.isLeaf = True
    
    ___ searchNode(self, word):
        children = self.root.children
        for c in word:
            __ c in children:
                t = children[c]
                children = t.children
            else:
                return None
        return t
    
    ___ search(self, word):
        t = self.searchNode(word)
        return bool(t and t.isLeaf)
    
    ___ startsWith(self, prefix):
        t = self.searchNode(prefix)
        return bool(t is not None)
    
    