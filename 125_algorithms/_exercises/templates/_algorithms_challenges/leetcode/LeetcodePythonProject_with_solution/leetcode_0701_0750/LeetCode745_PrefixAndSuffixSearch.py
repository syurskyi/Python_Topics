'''
Created on Mar 22, 2018

@author: tongq
'''
class TreeNode(object):
    ___ __init__(self, val):
        self.val = val
        self.children = {}
        self.isLeaf = False
        self.candidates = set()

class WordFilter(object):

    ___ __init__(self, words):
        """
        :type words: List[str]
        """
        self.root1 = TreeNode('')
        self.root2 = TreeNode('')
        self.buildTree(self.root1, words, False)
        self.buildTree(self.root2, words, True)
    
    ___ buildTree(self, root, words, reverse):
        ___ i0, word __ e..(words):
            __ reverse:
                word = word[::-1]
            node = root
            node.candidates.add(i0)
            ___ i, c __ e..(word):
                __ c n.. __ node.children:
                    node.children[c] = TreeNode('')
                node = node.children[c]
                node.candidates.add(i0)
                __ i __ l..(word)-1:
                    node.isLeaf = True
    
    ___ f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        cand1 = self.helper(self.root1, prefix)
        cand2 = self.helper(self.root2, suffix[::-1])
        res = -1
        ___ i __ cand1:
            __ i __ cand2:
                res = max(res, i)
        r.. res
    
    ___ helper(self, root, word):
        __ n.. word:
            r.. root.candidates
        ___ i, c __ e..(word):
            __ c n.. __ root.children:
                r.. set()
            root = root.children[c]
            __ i __ l..(word)-1:
                r.. root.candidates

__ __name__ __ '__main__':
    wordFilter = WordFilter(["abbbababbb","baaabbabbb","abababbaaa","abbbbbbbba","bbbaabbbaa","ababbaabaa","baaaaabbbb","babbabbabb","ababaababb","bbabbababa"])
    res = wordFilter.f("","abaa")
    print('res: %s' % res)
