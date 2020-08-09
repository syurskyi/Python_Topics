'''
Created on Sep 27, 2017

@author: MT
'''
class TreeNode(object
    ___ __init__(self, val
        self.val = val
        self.children = {}
        self.candidates = {}
        self.isLeaf = False

class AutocompleteSystem(object

    ___ __init__(self, sentences, times
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.root = TreeNode(None)
        self.node = self.root
        self.s = ''
        ___ s, count in zip(sentences, times
            node = self.root
            ___ c in s:
                __ c not in node.children:
                    newNode = TreeNode(c)
                    node.children[c] = newNode
                node = node.children[c]
                node.candidates[s] = node.candidates.get(s, 0)+count
            node.isLeaf = True

    ___ input(self, c
        """
        :type c: str
        :rtype: List[str]
        """
        __ c __ '#':
            res = []
            self.node = self.root
            self.addCandidate(self.s)
            self.s = ''
            r_ res
        ____
            self.s += c
            __ self.node and c in self.node.children:
                node = self.node.children[c]
                self.node = node
                candidates = node.candidates
                res = [(-count, s) ___ s, count in candidates.items()]
                res.sort()
                res = res[:3]
                r_ [s ___ count, s in res]
            ____
                self.node = None
                r_ []
    
    ___ addCandidate(self, s
        node = self.root
        ___ c in s:
            __ c not in node.children:
                newNode = TreeNode(c)
                node.children[c] = newNode
            node = node.children[c]
            node.candidates[s] = node.candidates.get(s, 0)+1
        node.isLeaf = True

__ __name__ __ '__main__':
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
