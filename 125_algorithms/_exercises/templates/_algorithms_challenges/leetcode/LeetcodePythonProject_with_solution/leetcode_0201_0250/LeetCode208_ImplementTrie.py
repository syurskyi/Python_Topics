'''
Created on Feb 18, 2017

@author: MT
'''

c_ TrieNode(o..
    ___ - , s N..
        c s
        children    # dict
        isLeaf F..

c_ Trie(o..
    ___ -
        root TrieNode()
    
    ___ insert  word
        children root.children
        ___ i, c __ e..(word
            __ c __ children:
                t children[c]
            ____
                t TrieNode(c)
                children[c] t
            children t.children
            __ i __ l..(word)-1:
                t.isLeaf T..
    
    ___ searchNode  word
        children root.children
        ___ c __ word:
            __ c __ children:
                t children[c]
                children t.children
            ____
                r.. N..
        r.. t
    
    ___ s..  word
        t searchNode(word)
        r.. b..(t a.. t.isLeaf)
    
    ___ startsWith  prefix
        t searchNode(prefix)
        r.. b..(t __ n.. N..)
    
    