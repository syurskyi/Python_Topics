'''
Created on Feb 19, 2017

@author: MT
'''

class TrieNode(object
    ___ __init__(self, c=None
        self.c = c
        self.children = {}
        self.isLeaf = False

class WordDictionary(object
    ___ __init__(self
        self.root = TrieNode()
    
    ___ addWord(self, word
        children = self.root.children
        for i, c in enumerate(word
            __ c in children:
                t = children[c]
            ____
                t = TrieNode(c)
                children[c] = t
            children = t.children
            __ i __ le.(word)-1:
                t.isLeaf = True
    
    ___ searchDFS(self, children, word, startInd
        __ startInd __ le.(word
            r_ bool(not children)
        c = word[startInd]
        __ c in children:
            __ startInd __ le.(word)-1 and children[c].isLeaf:
                r_ True
            r_ self.searchDFS(children[c].children, word, startInd+1)
        ____ c __ '.':
            for key, node in children.iteritems(
                __ startInd __ le.(word)-1 and node.isLeaf:
                    r_ True
                __ self.searchDFS(children[key].children, word, startInd+1
                    r_ True
            r_ False
        ____
            r_ False
    
    ___ search(self, word
        r_ self.searchDFS(self.root.children, word, 0)
    