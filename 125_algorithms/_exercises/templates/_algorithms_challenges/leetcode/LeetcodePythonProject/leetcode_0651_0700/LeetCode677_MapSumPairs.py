'''
Created on Oct 18, 2017

@author: MT
'''
class TreeNode(object
    ___ __init__(self, val
        self.val = val
        self.su. = 0
        self.children = {}

class MapSum(object

    ___ __init__(self
        """
        Initialize your data structure here.
        """
        self.hashmap = {}
        self.root = TreeNode(None)

    ___ insert(self, key, val
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        diff = 0
        __ key in self.hashmap:
            diff = -self.hashmap[key]
        self.hashmap[key] = val
        node = self.root
        ___ c in key:
            __ c not in node.children:
                newNode = TreeNode(c)
                node.children[c] = newNode
            node = node.children[c]
            node.su. += val+diff

    ___ su.(self, prefix
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        ___ c in prefix:
            __ c not in node.children:
                r_ 0
            node = node.children[c]
        r_ node.su.

__ __name__ __ '__main__':
    mapSum = MapSum()
    mapSum.insert('aa', 3)
    mapSum.insert('aa', 2)
    print(mapSum.su.('a'))
