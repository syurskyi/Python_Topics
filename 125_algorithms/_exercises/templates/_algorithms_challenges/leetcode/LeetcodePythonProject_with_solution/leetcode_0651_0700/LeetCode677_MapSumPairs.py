'''
Created on Oct 18, 2017

@author: MT
'''
class TreeNode(object):
    ___ __init__(self, val):
        self.val = val
        self.sum = 0
        self.children = {}

class MapSum(object):

    ___ __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {}
        self.root = TreeNode(None)

    ___ insert(self, key, val):
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
        for c in key:
            __ c not in node.children:
                newNode = TreeNode(c)
                node.children[c] = newNode
            node = node.children[c]
            node.sum += val+diff

    ___ sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        for c in prefix:
            __ c not in node.children:
                return 0
            node = node.children[c]
        return node.sum

__ __name__ == '__main__':
    mapSum = MapSum()
    mapSum.insert('aa', 3)
    mapSum.insert('aa', 2)
    print(mapSum.sum('a'))
