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
        for i, c in enumerate(word):
            __ c in children:
                t = children[c]
            else:
                t = TrieNode(c)
                children[c] = t
            children = t.children
            __ i == len(word)-1:
                t.isLeaf = True
    
    ___ searchDFS(self, children, word, startInd):
        __ startInd == len(word):
            return bool(not children)
        c = word[startInd]
        __ c in children:
            __ startInd == len(word)-1 and children[c].isLeaf:
                return True
            return self.searchDFS(children[c].children, word, startInd+1)
        elif c == '.':
            for key, node in children.iteritems():
                __ startInd == len(word)-1 and node.isLeaf:
                    return True
                __ self.searchDFS(children[key].children, word, startInd+1):
                    return True
            return False
        else:
            return False
    
    ___ search(self, word):
        return self.searchDFS(self.root.children, word, 0)
    