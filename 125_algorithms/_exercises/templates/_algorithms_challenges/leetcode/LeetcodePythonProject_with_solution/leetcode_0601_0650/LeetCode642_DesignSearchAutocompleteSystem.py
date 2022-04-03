'''
Created on Sep 27, 2017

@author: MT
'''
c_ TreeNode(o..
    ___ - , val
        val = val
        children    # dict
        candidates    # dict
        isLeaf = F..

c_ AutocompleteSystem(o..

    ___ - , sentences, times
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        root = TreeNode(N..)
        node = root
        s = ''
        ___ s, count __ z..(sentences, times
            node = root
            ___ c __ s:
                __ c n.. __ node.children:
                    newNode = TreeNode(c)
                    node.children[c] = newNode
                node = node.children[c]
                node.candidates[s] = node.candidates.g.. s, 0)+count
            node.isLeaf = T..

    ___ input  c
        """
        :type c: str
        :rtype: List[str]
        """
        __ c __ '#':
            res    # list
            node = root
            addCandidate(s)
            s = ''
            r.. res
        ____:
            s += c
            __ node a.. c __ node.children:
                node = node.children[c]
                node = node
                candidates = node.candidates
                res = [(-count, s) ___ s, count __ candidates.i..]
                res.s..()
                res = res[:3]
                r.. [s ___ count, s __ res]
            ____:
                node = N..
                r.. []
    
    ___ addCandidate  s
        node = root
        ___ c __ s:
            __ c n.. __ node.children:
                newNode = TreeNode(c)
                node.children[c] = newNode
            node = node.children[c]
            node.candidates[s] = node.candidates.g.. s, 0)+1
        node.isLeaf = T..

__ _____ __ _____
#     autoSys = AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
#     print(autoSys.input('i'))
#     print(autoSys.input(' '))
#     print(autoSys.input('a'))
#     print(autoSys.input('#'))

#     autoSys = AutocompleteSystem(["i love you","island","iroman","i love leetcode"],[5,3,2,2])
#     print(autoSys.input("i"))
#     print(autoSys.input(" "))
#     print(autoSys.input("a"))
#     print(autoSys.input("#"))
#     print(autoSys.input("i"))
#     print(autoSys.input(" "))
#     print(autoSys.input("a"))
#     print(autoSys.input("#"))
#     print(autoSys.input("i"))
#     print(autoSys.input(" "))
#     print(autoSys.input("a"))
#     print(autoSys.input("#"))

    autoSys = AutocompleteSystem(["abc","abbc","a"],[3,3,3])
    print(autoSys.input("b"))
    print(autoSys.input("c"))
    print(autoSys.input("#"))
    print(autoSys.input("b"))
    print(autoSys.input("c"))
    print(autoSys.input("#"))
    print(autoSys.input("a"))
    print(autoSys.input("b"))
    print(autoSys.input("c"))
    print(autoSys.input("#"))
    print(autoSys.input("a"))
    print(autoSys.input("b"))
    print(autoSys.input("c"))
    print(autoSys.input("#"))
