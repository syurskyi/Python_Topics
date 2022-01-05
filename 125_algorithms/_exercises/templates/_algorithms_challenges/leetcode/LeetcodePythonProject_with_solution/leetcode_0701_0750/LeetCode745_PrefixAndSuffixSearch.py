'''
Created on Mar 22, 2018

@author: tongq
'''
c_ TreeNode(o..):
    ___ - , val):
        val = val
        children    # dict
        isLeaf = F..
        candidates = set()

c_ WordFilter(o..):

    ___ - , words):
        """
        :type words: List[str]
        """
        root1 = TreeNode('')
        root2 = TreeNode('')
        buildTree(root1, words, F..)
        buildTree(root2, words, T..)
    
    ___ buildTree  root, words, reverse):
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
                    node.isLeaf = T..
    
    ___ f  prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        cand1 = helper(root1, prefix)
        cand2 = helper(root2, suffix[::-1])
        res = -1
        ___ i __ cand1:
            __ i __ cand2:
                res = m..(res, i)
        r.. res
    
    ___ helper  root, word):
        __ n.. word:
            r.. root.candidates
        ___ i, c __ e..(word):
            __ c n.. __ root.children:
                r.. set()
            root = root.children[c]
            __ i __ l..(word)-1:
                r.. root.candidates

__ _____ __ _____
    wordFilter = WordFilter(["abbbababbb","baaabbabbb","abababbaaa","abbbbbbbba","bbbaabbbaa","ababbaabaa","baaaaabbbb","babbabbabb","ababaababb","bbabbababa"])
    res = wordFilter.f("","abaa")
    print('res: %s' % res)
